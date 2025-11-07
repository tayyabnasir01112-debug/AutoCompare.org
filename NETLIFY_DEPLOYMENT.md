# Netlify Deployment - Quick Start

## Current Configuration

✅ **Build verified**: Production build successful
✅ **Output directory**: `frontend/dist` contains all files
✅ **Netlify config**: `netlify.toml` configured correctly

## Deployment Configuration

### Netlify Settings (from `netlify.toml`)

```toml
Build command: npm run build
Publish directory: frontend/dist
Root directory: . (project root)
Node version: 20
```

### Build Output Verification

```
frontend/dist/
├── index.html              ✅ Homepage
├── about/index.html        ✅ About page
├── blog/index.html         ✅ Blog index
├── blog/[...slug]/         ✅ Blog posts
├── data/prices.json        ✅ Price data
├── sitemap-index.xml       ✅ Sitemap
├── rss.xml                 ✅ RSS feed
└── _astro/                 ✅ Assets
```

## Quick Deploy Steps

### 1. Push to GitHub

```bash
git add .
git commit -m "Ready for Netlify deployment"
git push origin main
```

### 2. Deploy to Netlify

#### Via Netlify UI:

1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Select your GitHub repository
4. Netlify auto-detects settings from `netlify.toml`
5. Click "Deploy site"

#### Via Netlify CLI:

```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod
```

### 3. Verify Deployment

After deployment:
- ✅ Site is accessible at `https://your-site.netlify.app`
- ✅ All pages load correctly
- ✅ Price data displays
- ✅ Blog posts accessible

### 4. Enable Automatic Deploys

1. Netlify dashboard → Site settings
2. Build & deploy → Continuous deployment
3. Enable "Deploy automatically"

## GitHub Actions Badge

After deployment, add this to your README.md:

```markdown
[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR_SITE_ID/deploy-status)](https://app.netlify.com/sites/YOUR_SITE_NAME/deploys)
```

**To get your badge URL:**
1. Netlify dashboard → Site settings → General
2. Scroll to "Status badges"
3. Copy the badge markdown

## Automated Deployment Flow

```
GitHub Push → Netlify Build → Deploy
     ↓
GitHub Actions (Scraper) → Update prices.json → Commit
     ↓
Netlify Auto-deploy → Rebuild site
```

## Custom Domain Setup

1. Netlify dashboard → Site settings → Domain management
2. Add custom domain (e.g., `autocompare.org`)
3. Follow DNS configuration instructions
4. Wait for DNS propagation (usually 24-48 hours)

## Troubleshooting

### Build Fails
- Check build logs in Netlify dashboard
- Verify Node version is 20
- Ensure `package.json` has build script

### Price Data Missing
- Run scraper: `python backend/scraper.py`
- Commit updated `frontend/public/data/prices.json`
- Push to trigger rebuild

### 404 Errors
- Verify redirect rules in `netlify.toml`
- Check that all routes redirect to `/index.html`

## Status

✅ **Ready for deployment**
✅ **Build verified**
✅ **Configuration complete**

---

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

