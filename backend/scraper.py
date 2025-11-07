import asyncio
import json
import aiofiles
from playwright.async_api import async_playwright
from datetime import datetime
from pathlib import Path

async def scrape_site(playwright, name, site):
    """
    Scrape a single site based on configuration.
    
    Args:
        playwright: Playwright instance
        name: Site name/identifier
        site: Site configuration dict with 'url' and 'selectors'
    
    Returns:
        dict: Scraped data including metadata
    """
    browser = None
    try:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Navigate to the URL with timeout
        await page.goto(site['url'], timeout=30000, wait_until='domcontentloaded')
        
        # Wait a bit for dynamic content
        await page.wait_for_timeout(2000)
        
        data = {
            'site': name,
            'url': site['url'],
            'scraped_at': datetime.now().isoformat(),
            'success': True,
            'data': {}
        }
        
        # Scrape each selector
        for key, selector in site['selectors'].items():
            try:
                element = await page.query_selector(selector)
                if element:
                    text = await element.text_content()
                    data['data'][key] = text.strip() if text else None
                else:
                    data['data'][key] = None
            except Exception as e:
                print(f"Error scraping {key} from {name}: {str(e)}")
                data['data'][key] = None
        
        return data
        
    except Exception as e:
        print(f"Error scraping {name}: {str(e)}")
        return {
            'site': name,
            'url': site['url'],
            'scraped_at': datetime.now().isoformat(),
            'success': False,
            'error': str(e),
            'data': {}
        }
    finally:
        if browser:
            await browser.close()

async def main():
    """Main scraper function that processes all configured sites."""
    
    # Ensure directories exist
    Path('backend/configs').mkdir(parents=True, exist_ok=True)
    Path('backend/data').mkdir(parents=True, exist_ok=True)
    Path('frontend/public/data').mkdir(parents=True, exist_ok=True)
    
    # Load site configurations
    config_file = 'backend/configs/sites.json'
    
    try:
        async with aiofiles.open(config_file, 'r') as f:
            sites = json.loads(await f.read())
    except FileNotFoundError:
        print(f"Configuration file not found: {config_file}")
        print("Please create a sites.json file with your scraping configurations.")
        return
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in configuration file: {e}")
        return
    
    if not sites:
        print("No sites configured for scraping.")
        return
    
    print(f"Starting scrape of {len(sites)} sites...")
    
    # Run scraper
    async with async_playwright() as p:
        results = {}
        
        # Scrape all sites (could be parallelized for better performance)
        for name, site in sites.items():
            print(f"Scraping {name}...")
            results[name] = await scrape_site(p, name, site)
            
            # Small delay between requests to be respectful
            await asyncio.sleep(1)
    
    # Save results to backend/data
    output_file = 'backend/data/prices.json'
    json_content = json.dumps(results, indent=2)
    
    async with aiofiles.open(output_file, 'w') as f:
        await f.write(json_content)
    
    # Also copy to frontend/public/data for static site access
    frontend_output = 'frontend/public/data/prices.json'
    async with aiofiles.open(frontend_output, 'w') as f:
        await f.write(json_content)
    
    print(f"\nScraping complete!")
    print(f"Results saved to:")
    print(f"  - {output_file}")
    print(f"  - {frontend_output}")
    
    # Print summary
    successful = sum(1 for r in results.values() if r.get('success', False))
    print(f"Successfully scraped: {successful}/{len(results)} sites")

if __name__ == '__main__':
    asyncio.run(main())
