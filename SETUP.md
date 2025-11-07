# AutoCompare.org Setup Guide

This guide will help you set up and test AutoCompare.org locally and prepare it for deployment.

## Prerequisites

- **Python 3.11+** (tested with 3.11 and 3.12)
- **Node.js 20+** and npm
- **Git** (for version control)

## Quick Setup

### 1. Install Dependencies

#### Backend (Python)
```bash
# Install Python dependencies
pip install -r requirements.txt

# Or install manually
pip install playwright aiofiles

# Install Playwright browsers
playwright install chromium
```

#### Frontend (Node.js)
```bash
# Install frontend dependencies
cd frontend
npm install
cd ..
```

Or use the convenience script:
```bash
npm run setup
```

### 2. Configure Sites to Scrape

Edit `backend/configs/sites.json` to add websites you want to scrape:

```json
{
  "product_name_1": {
    "url": "https://www.example.com/product/123",
    "selectors": {
      "title": "h1.product-title",
      "price": ".price",
      "description": ".product-description"
    }
  }
}
```

**How to find CSS selectors:**
1. Open the product page in your browser
2. Right-click the element → Inspect
3. Find a unique CSS selector (ID or class)
4. Test with `document.querySelector('YOUR_SELECTOR')` in browser console

### 3. Test the Scraper

```bash
# Test scraper configuration
python backend/test-scraper.py

# Run the full scraper
python backend/scraper.py
```

This will:
- Validate your configuration
- Scrape all configured sites
- Save results to `backend/data/prices.json`
- Copy data to `frontend/public/data/prices.json`

### 4. Test the Frontend

```bash
# Test frontend setup
node test-frontend.js

# Start development server
npm run dev
# or
cd frontend && npm run dev
```

Visit `http://localhost:5000` to see your site.

### 5. Build for Production

```bash
# Build the frontend
npm run build
# or
cd frontend && npm run build

# Preview the build
npm run preview
```

## Running Tests

```bash
# Test both backend and frontend
npm test

# Test scraper only
npm run test:scraper

# Test frontend only
npm run test:frontend
```

## Deployment

### Netlify Deployment

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
   - Netlify will auto-detect settings from `netlify.toml`
   - Click "Deploy site"

3. **Custom Domain** (Optional)
   - In Netlify dashboard: Site settings → Domain management
   - Add your custom domain
   - Follow DNS configuration steps

### Automated Scraping

The GitHub Actions workflow automatically runs daily at midnight UTC.

**To enable:**
- Ensure your repository has GitHub Actions enabled
- The workflow will run automatically
- Check the "Actions" tab to monitor runs

**Manual trigger:**
- Go to Actions tab → "Daily Price Scraper" → "Run workflow"

## Troubleshooting

### Scraper Issues

**Problem:** Scraper returns null values
- **Solution:** Verify CSS selectors using browser inspector
- **Tip:** Some sites use dynamic selectors - try more stable alternatives

**Problem:** Playwright fails to launch
- **Solution:** Ensure Chromium is installed: `playwright install chromium`
- **Linux:** May need system dependencies: `playwright install-deps chromium`

**Problem:** Permission errors on Windows
- **Solution:** Run PowerShell/Command Prompt as Administrator
- **Alternative:** Use WSL (Windows Subsystem for Linux)

### Frontend Issues

**Problem:** Price data doesn't show on homepage
- **Solution:** Ensure `frontend/public/data/prices.json` exists
- **Check:** Run the scraper at least once before building
- **Verify:** Check browser console for errors

**Problem:** Build fails on Netlify
- **Solution:** Check build logs for missing dependencies
- **Verify:** `netlify.toml` has correct build command
- **Ensure:** Node version is 20+ (configured in netlify.toml)

**Problem:** "Price data not available" message
- **Solution:** This is normal if you haven't run the scraper yet
- **Fix:** Run `python backend/scraper.py` to generate initial data

### GitHub Actions Issues

**Problem:** Workflow fails to commit
- **Solution:** Ensure repository has write permissions enabled
- **Check:** Repository Settings → Actions → General → Workflow permissions
- **Verify:** "Read and write permissions" is selected

**Problem:** Workflow can't find files
- **Solution:** Ensure paths are correct in the workflow file
- **Check:** File paths are relative to repository root

## Project Structure

```
AutoCompareUniversal/
├── backend/
│   ├── configs/
│   │   └── sites.json          # Scraper configuration
│   ├── data/
│   │   └── prices.json         # Scraped price data
│   ├── scraper.py              # Main scraper script
│   └── test-scraper.py         # Scraper test script
├── frontend/
│   ├── public/
│   │   └── data/
│   │       └── prices.json     # Price data (for frontend)
│   ├── src/
│   │   ├── pages/
│   │   │   └── index.astro     # Homepage
│   │   └── ...
│   └── package.json
├── .github/
│   └── workflows/
│       └── scrape.yml          # GitHub Actions workflow
├── netlify.toml                # Netlify deployment config
├── requirements.txt            # Python dependencies
├── package.json                # Root-level convenience scripts
└── README.md
```

## Next Steps

1. ✅ Configure sites in `backend/configs/sites.json`
2. ✅ Test scraper: `python backend/test-scraper.py`
3. ✅ Run scraper: `python backend/scraper.py`
4. ✅ Test frontend: `npm run test:frontend`
5. ✅ Start dev server: `npm run dev`
6. ✅ Build for production: `npm run build`
7. ✅ Deploy to Netlify
8. ✅ Enable GitHub Actions for automated scraping

## Support

For issues and questions:
- Check the main [README.md](README.md) for detailed documentation
- Review [QUICKSTART.md](QUICKSTART.md) for quick reference
- Open an issue on GitHub

---

**Happy scraping! 🛍️**

