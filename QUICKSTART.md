# AutoCompare.org - Quick Start Guide

Get your price comparison website running in 5 minutes!

## Local Development

### 1. Install Dependencies

Python dependencies are already installed. Frontend dependencies:
```bash
cd frontend
npm install
```

### 2. Run the Development Server

```bash
cd frontend
npm run dev
```

Visit `http://localhost:5000` to see your site.

## Customize Your Site

### Add Products to Compare

Edit `backend/configs/sites.json`:

```json
{
  "amazon_laptop": {
    "url": "https://www.amazon.com/dp/YOUR_PRODUCT_ID",
    "selectors": {
      "title": "#productTitle",
      "price": ".a-price-whole",
      "description": "#feature-bullets"
    }
  }
}
```

**How to find CSS selectors:**
1. Open the product page in Chrome/Firefox
2. Right-click the element you want to scrape → Inspect
3. Find a unique CSS selector (ID or class)
4. Test with `document.querySelector('YOUR_SELECTOR')` in browser console

### Run the Scraper

```bash
python backend/scraper.py
```

Data will be saved to:
- `backend/data/prices.json`
- `frontend/public/data/prices.json`

### Add Blog Posts

Create a new file in `frontend/src/content/blog/`:

```markdown
---
title: 'Your Post Title'
description: 'SEO description'
pubDate: 'Nov 07 2025'
---

Your content here...
```

## Deploy to Production

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/autocompare.git
git push -u origin main
```

### 2. Deploy to Netlify

1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Select your GitHub repo
4. Netlify auto-detects settings from `netlify.toml`
5. Click "Deploy site"

### 3. Add Custom Domain (Optional)

In Netlify dashboard:
- Site settings → Domain management
- Add your domain
- Follow DNS configuration steps

## Automation

The scraper runs automatically every day at midnight UTC via GitHub Actions.

**Manual run:**
- Go to your GitHub repo → Actions tab
- Select "Daily Price Scraper" → "Run workflow"

## Troubleshooting

**Problem:** Scraper returns null values  
**Solution:** Check CSS selectors are correct using browser inspector

**Problem:** Frontend shows "No price data available"  
**Solution:** Run `python backend/scraper.py` to generate initial data

**Problem:** Build fails on Netlify  
**Solution:** Check the build logs, ensure all dependencies are listed

## Next Steps

- Update `backend/configs/sites.json` with real products
- Write more blog posts for SEO
- Customize styling in `frontend/src/pages/index.astro`
- Monitor GitHub Actions for scraping success

**Need help?** Check the full README.md for detailed documentation.
