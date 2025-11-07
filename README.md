# AutoCompare.org - Automated Price Comparison Website

[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR_SITE_ID/deploy-status)](https://app.netlify.com/sites/YOUR_SITE_NAME/deploys)

**AutoCompare.org** is a fully automated price comparison platform with integrated blog functionality. Built with Astro for blazing-fast performance and Python + Playwright for universal web scraping.

## Features

- **Universal Web Scraper**: JSON-configured Playwright scraper that works with any website
- **Automated Daily Updates**: GitHub Actions runs scraper every midnight UTC
- **SEO-Optimized Blog**: Markdown-based blog system for shopping guides and reviews
- **Modern Frontend**: Astro static site with excellent performance scores
- **Zero-Cost Hosting**: Deployable to Netlify's free tier
- **Price Comparison UI**: Clean, responsive interface for comparing product prices

## Tech Stack

### Frontend
- **Astro 5.x**: Static site generator with excellent SEO
- **Markdown/MDX**: Easy content management for blog posts
- **Responsive Design**: Mobile-friendly price comparison cards

### Backend
- **Python 3.11**: Scraper engine
- **Playwright**: Headless browser automation
- **Aiofiles**: Async file operations for performance

### Automation & Deployment
- **GitHub Actions**: Daily automated scraping
- **Netlify**: Free hosting with CDN and custom domains
- **Git**: Version control and data storage

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Git

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd autocompare-org
```

2. **Install Python dependencies**
```bash
pip install playwright aiofiles
playwright install chromium
```

3. **Install frontend dependencies**
```bash
cd frontend
npm install
```

### Configuration

#### 1. Configure Sites to Scrape

Edit `backend/configs/sites.json` to add websites you want to scrape:

```json
{
  "amazon_laptop": {
    "url": "https://www.amazon.com/dp/PRODUCT_ID",
    "selectors": {
      "title": "#productTitle",
      "price": ".a-price-whole",
      "description": "#feature-bullets"
    }
  },
  "bestbuy_laptop": {
    "url": "https://www.bestbuy.com/site/product/PRODUCT_ID",
    "selectors": {
      "title": "h1.heading-5",
      "price": ".priceView-customer-price span",
      "description": ".item-description"
    }
  }
}
```

**How to find selectors:**
1. Open the product page in your browser
2. Right-click the element you want to scrape
3. Select "Inspect" to see the HTML
4. Identify a unique CSS selector for that element

#### 2. Run the Scraper Locally

```bash
python backend/scraper.py
```

This will scrape all configured sites and save results to `backend/data/prices.json`.

#### 3. Start the Development Server

```bash
cd frontend
npm run dev
```

Visit `http://localhost:5000` to see your site.

### Creating Blog Posts

Add new blog posts to `frontend/src/content/blog/`:

```markdown
---
title: 'Your Blog Post Title'
description: 'SEO-friendly description'
pubDate: 'Nov 07 2025'
heroImage: '/blog-placeholder-1.jpg'
---

Your markdown content here...
```

## Deployment

### Deploy to Netlify

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo>
git push -u origin main
```

2. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Select your GitHub repository
   - Netlify will auto-detect the `netlify.toml` configuration
   - Click "Deploy site"

3. **Custom Domain** (Optional)
   - In Netlify dashboard: Site settings → Domain management
   - Add your custom domain (e.g., autocompare.org)
   - Follow Netlify's DNS configuration instructions

### Enable Automated Scraping

The GitHub Actions workflow automatically runs daily at midnight UTC.

**To enable it:**
1. Ensure your repository is public OR you have GitHub Actions enabled
2. The workflow will run automatically
3. Check the "Actions" tab in GitHub to monitor runs

**Manual trigger:**
- Go to Actions tab → "Daily Price Scraper" → "Run workflow"

## Project Structure

```
autocompare-org/
├── backend/
│   ├── configs/
│   │   └── sites.json          # Scraper configuration
│   ├── data/
│   │   └── prices.json         # Scraped price data
│   └── scraper.py              # Main scraper script
├── frontend/
│   ├── src/
│   │   ├── components/         # Astro components
│   │   ├── content/
│   │   │   └── blog/           # Blog posts (markdown)
│   │   ├── layouts/            # Page layouts
│   │   └── pages/
│   │       ├── index.astro     # Homepage with price comparison
│   │       └── blog/           # Blog pages
│   ├── public/                 # Static assets
│   └── astro.config.mjs        # Astro configuration
├── .github/
│   └── workflows/
│       └── scrape.yml          # GitHub Actions workflow
├── netlify.toml                # Netlify deployment config
└── README.md
```

## Customization

### Adding More Products

1. Edit `backend/configs/sites.json`
2. Add new entries with URL and CSS selectors
3. Run the scraper to test
4. Commit and push to trigger automatic updates

### Styling the Frontend

- Edit `frontend/src/pages/index.astro` for homepage layout
- Modify styles in the `<style>` blocks
- Update `frontend/src/consts.ts` for site metadata

### SEO Optimization

- Add relevant keywords to blog posts
- Update meta descriptions in frontmatter
- Configure `astro.config.mjs` site URL
- Submit sitemap to search engines (auto-generated at `/sitemap-index.xml`)

## Troubleshooting

### Scraper Issues

**Problem**: Scraper returns null values
- **Solution**: Verify CSS selectors are correct using browser inspector
- **Tip**: Some sites use dynamic selectors - try more stable alternatives

**Problem**: Playwright fails to launch
- **Solution**: Ensure Chromium dependencies are installed
- **Command**: `playwright install-deps chromium`

### Frontend Issues

**Problem**: Price data doesn't show on homepage
- **Solution**: Ensure `backend/data/prices.json` exists and has valid data
- **Check**: Run the scraper at least once before building

**Problem**: Build fails on Netlify
- **Solution**: Check build logs for missing dependencies
- **Verify**: `netlify.toml` has correct build command

## Best Practices

### Ethical Scraping
- Respect robots.txt
- Add delays between requests (configured in scraper)
- Only scrape publicly available data
- Don't overload servers with requests

### Performance
- Keep site configurations to 10-20 products max
- Optimize images for faster loading
- Use Astro's built-in optimizations

### Maintenance
- Monitor GitHub Actions for scraper failures
- Update selectors when websites change layouts
- Regularly add fresh blog content for SEO

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Support

For questions and support, please open an issue on GitHub.

---

**Built with love for smart shoppers everywhere** 🛍️
