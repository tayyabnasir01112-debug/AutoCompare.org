# AutoCompare.org - Netlify Deployment Guide

## Pre-Deployment Checklist

✅ **Build Verification**
- [x] Production build tested locally: `npm run build`
- [x] Build output verified: `frontend/dist` contains all files
- [x] Price data included: `frontend/dist/data/prices.json` exists
- [x] All pages generated: 6 pages built successfully

✅ **Configuration Verified**
- [x] `netlify.toml` configured correctly
- [x] Build command: `npm run build`
- [x] Publish directory: `frontend/dist`
- [x] Node version: 20
- [x] Root directory: Project root (`.`)

## Deployment Steps

### Step 1: Verify Build Locally

```bash
# From project root
npm run build

# Verify output
ls frontend/dist
```

**Expected output:**
- `index.html`
- `about/`, `blog/` directories
- `data/prices.json`
- `_astro/` (assets)
- `sitemap-index.xml`

### Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Netlify deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/autocompare-org.git

# Push to main branch
git push -u origin main
```

### Step 3: Deploy to Netlify

#### Option A: Netlify UI (Recommended)

1. **Go to Netlify**
   - Visit [netlify.com](https://netlify.com)
   - Sign in or create an account

2. **Import Project**
   - Click "Add new site" → "Import an existing project"
   - Select "GitHub" and authorize Netlify
   - Choose your repository

3. **Configure Build Settings**
   - Netlify will auto-detect settings from `netlify.toml`
   - Verify:
     - **Base directory**: `.` (project root)
     - **Build command**: `npm run build`
     - **Publish directory**: `frontend/dist`
     - **Node version**: `20` (auto-detected)

4. **Deploy**
   - Click "Deploy site"
   - Wait for build to complete (~2-3 minutes)

5. **Verify Deployment**
   - Check build logs for success
   - Visit the generated URL (e.g., `https://random-name-123.netlify.app`)
   - Test all pages work correctly

#### Option B: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy
netlify deploy --prod

# Follow prompts to link site or create new site
```

### Step 4: Configure Site Settings

1. **Site Name** (Optional)
   - Site settings → Change site name
   - Choose a custom name (e.g., `autocompare-org`)

2. **Custom Domain** (Optional)
   - Site settings → Domain management
   - Add custom domain (e.g., `autocompare.org`)
   - Follow DNS configuration instructions

3. **Environment Variables** (If needed)
   - Site settings → Environment variables
   - Currently none required

### Step 5: Enable Automatic Deploys

1. **Auto-deploy on push**
   - Site settings → Build & deploy
   - Branch to deploy: `main`
   - Deploy contexts: Production

2. **Deploy hooks** (Optional)
   - Site settings → Build & deploy → Deploy hooks
   - Create hook for manual deployments

## Netlify Configuration

### Current Configuration (`netlify.toml`)

```toml
[build]
  publish = "frontend/dist"
  command = "npm run build"
  base = "."

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "20"
```

### Build Process

1. Netlify installs Node.js 20
2. Runs `npm install` (installs root dependencies)
3. Runs `npm run build` (builds frontend)
4. Publishes `frontend/dist` to CDN

### Redirect Rules

- All routes (`/*`) redirect to `/index.html` (SPA routing)
- Status 200 (clean URLs)

## GitHub Actions Integration

### Automated Scraping

The GitHub Actions workflow automatically:
1. Runs scraper daily at midnight UTC
2. Updates `backend/data/prices.json`
3. Updates `frontend/public/data/prices.json`
4. Commits and pushes changes
5. Triggers Netlify rebuild (if auto-deploy enabled)

### Enable GitHub Actions

1. **Repository Settings**
   - Settings → Actions → General
   - Enable "Read and write permissions"
   - Allow GitHub Actions to create commits

2. **Workflow Permissions**
   - Already configured in `.github/workflows/scrape.yml`
   - Has `contents: write` permission

3. **Test Workflow**
   - Go to Actions tab
   - Run "Daily Price Scraper" manually
   - Verify it commits updated prices

## Post-Deployment Verification

### ✅ Checklist

- [ ] Site is accessible at Netlify URL
- [ ] Homepage loads correctly
- [ ] Price data displays on homepage
- [ ] Blog posts are accessible
- [ ] About page loads
- [ ] All images load correctly
- [ ] Sitemap is accessible (`/sitemap-index.xml`)
- [ ] RSS feed works (`/rss.xml`)
- [ ] Mobile responsive design works

### Testing URLs

```
https://your-site.netlify.app/
https://your-site.netlify.app/about
https://your-site.netlify.app/blog
https://your-site.netlify.app/blog/best-laptops-2025
https://your-site.netlify.app/sitemap-index.xml
https://your-site.netlify.app/rss.xml
```

## Troubleshooting

### Build Fails

**Problem**: Build fails on Netlify
- **Solution**: Check build logs
- **Common issues**:
  - Missing dependencies (ensure `package.json` is in root)
  - Node version mismatch (verify `NODE_VERSION = "20"`)
  - Build command error (test locally first)

### Price Data Not Showing

**Problem**: Prices don't appear on homepage
- **Solution**: Ensure `frontend/public/data/prices.json` exists
- **Fix**: Run scraper before deploying: `python backend/scraper.py`
- **Verify**: Check `frontend/dist/data/prices.json` in build output

### 404 Errors

**Problem**: Pages return 404
- **Solution**: Verify redirect rules in `netlify.toml`
- **Check**: All routes should redirect to `/index.html`

### GitHub Actions Not Triggering Deploy

**Problem**: Scraper updates don't trigger Netlify rebuild
- **Solution**: Enable "Deploy notifications" in Netlify
- **Alternative**: Use Netlify build hook in GitHub Actions

## Deployment Badge

Add to README.md:

```markdown
[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR_SITE_ID/deploy-status)](https://app.netlify.com/sites/YOUR_SITE_NAME/deploys)
```

Get your badge URL from:
- Netlify dashboard → Site settings → General → Status badges

## Next Steps

1. ✅ **Deploy to Netlify** (completed)
2. ⏳ **Configure custom domain** (optional)
3. ⏳ **Set up analytics** (optional)
4. ⏳ **Configure form handling** (if needed)
5. ⏳ **Set up monitoring** (optional)

## Support

For deployment issues:
- Check [Netlify Docs](https://docs.netlify.com)
- Review build logs in Netlify dashboard
- Check GitHub Actions logs
- Review project documentation

---

**Status**: ✅ Ready for deployment
**Last Updated**: 2025-11-07

