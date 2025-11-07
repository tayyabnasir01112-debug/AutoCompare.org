#!/usr/bin/env python3
"""
Test script for the AutoCompare scraper.
This script validates the scraper configuration and tests a single site scrape.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path to import scraper
sys.path.insert(0, str(Path(__file__).parent))

from scraper import scrape_site, PROJECT_ROOT
from playwright.async_api import async_playwright

async def test_config():
    """Test if the configuration file exists and is valid."""
    config_file = PROJECT_ROOT / 'backend' / 'configs' / 'sites.json'
    
    print("=" * 60)
    print("Testing Scraper Configuration")
    print("=" * 60)
    
    if not config_file.exists():
        print(f"[FAIL] Configuration file not found: {config_file}")
        print("\nPlease create backend/configs/sites.json with your scraping configurations.")
        return (False, None)
    
    try:
        with open(config_file, 'r') as f:
            sites = json.load(f)
        
        if not sites:
            print("[FAIL] No sites configured in sites.json")
            return (False, None)
        
        print(f"[OK] Configuration file found: {config_file}")
        print(f"[OK] Found {len(sites)} site(s) configured")
        
        # List configured sites
        print("\nConfigured sites:")
        for name, site in sites.items():
            print(f"  - {name}: {site.get('url', 'N/A')}")
        
        return (True, sites)
        
    except json.JSONDecodeError as e:
        print(f"[FAIL] Invalid JSON in configuration file: {e}")
        return (False, None)

async def test_scrape_one_site(name, site):
    """Test scraping a single site."""
    print("\n" + "=" * 60)
    print(f"Testing scrape: {name}")
    print("=" * 60)
    
    try:
        async with async_playwright() as p:
            result = await scrape_site(p, name, site)
            
            if result['success']:
                print(f"[OK] Successfully scraped {name}")
                print(f"\nResults:")
                print(f"  URL: {result['url']}")
                print(f"  Scraped at: {result['scraped_at']}")
                print(f"  Data extracted:")
                for key, value in result['data'].items():
                    status = "[OK]" if value else "[FAIL]"
                    print(f"    {status} {key}: {value[:50] if value else 'None'}...")
                return True
            else:
                print(f"[FAIL] Failed to scrape {name}")
                print(f"  Error: {result.get('error', 'Unknown error')}")
                return False
                
    except Exception as e:
        print(f"[FAIL] Error during scraping: {str(e)}")
        return False

async def main():
    """Main test function."""
    print("\n" + "=" * 60)
    print("AutoCompare Scraper Test Suite")
    print("=" * 60 + "\n")
    
    # Test configuration
    config_result = await test_config()
    if not config_result or not config_result[0]:
        sys.exit(1)
    
    _, sites = config_result
    
    # Test scraping first site
    if sites:
        first_name = list(sites.keys())[0]
        first_site = sites[first_name]
        
        print(f"\nTesting scrape of first site: {first_name}")
        scrape_result = await test_scrape_one_site(first_name, first_site)
        
        if scrape_result:
            print("\n" + "=" * 60)
            print("[SUCCESS] Test completed successfully!")
            print("=" * 60)
            print("\nYou can now run the full scraper with:")
            print("  python backend/scraper.py")
        else:
            print("\n" + "=" * 60)
            print("[FAIL] Test failed - please check your configuration")
            print("=" * 60)
            sys.exit(1)
    else:
        print("No sites to test")
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())

