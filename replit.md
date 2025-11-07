# AutoCompare.org

## Overview

AutoCompare.org is an automated price comparison platform that combines web scraping with content publishing. The system automatically scrapes product prices from multiple websites daily and presents them through a fast, SEO-optimized frontend. It also includes a markdown-based blog for shopping guides and product reviews.

The architecture is designed for zero-cost deployment, leveraging static site generation for the frontend and GitHub Actions for automated scraping, with all data stored as JSON files in the repository.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Static Site Generation with Astro 5.x**
- **Problem**: Need fast, SEO-friendly pages with excellent performance scores
- **Solution**: Astro static site generator that pre-renders all pages at build time
- **Rationale**: Astro provides near-perfect Lighthouse scores, built-in SEO features, and minimal JavaScript in production
- **Content Management**: Markdown/MDX files in `src/content/blog/` for blog posts with frontmatter-based metadata (title, description, pubDate, heroImage)
- **Build Output**: Static HTML/CSS/JS deployed to CDN (Netlify)

**Data Display Strategy**
- **Problem**: Display dynamically scraped price data in a static site
- **Solution**: JSON file in `frontend/public/data/prices.json` that gets included in the build
- **Workflow**: Scraper updates JSON → triggers rebuild → new static site with updated prices
- **Pros**: No backend needed, extremely fast page loads, works on free hosting
- **Cons**: Requires rebuild for data updates (acceptable for daily updates)

**Content Collections Pattern**
- Blog posts use Astro's content collections with TypeScript schema validation
- Type-safe frontmatter ensures consistency across blog posts
- Automatic RSS feed generation for blog subscribers

### Backend Architecture

**Python + Playwright Web Scraper**
- **Problem**: Need to scrape product data from various websites with different structures
- **Solution**: Configuration-driven scraper using `backend/configs/sites.json`
- **Key Features**:
  - Each site configuration includes URL and CSS selectors for data extraction
  - Headless Chromium browser automation via Playwright
  - Async operations with aiofiles for performance
  - Error handling per selector (continues if one element fails)
  - Metadata tracking (timestamp, success status)

**Scraper Configuration Format**
```json
{
  "site_name": {
    "url": "https://example.com/product",
    "selectors": {
      "title": "h1",
      "price": ".price",
      "description": ".description"
    }
  }
}
```

**Data Flow**
1. Python script reads `backend/configs/sites.json`
2. For each site, launches headless browser and navigates to URL
3. Waits for dynamic content (2 second delay)
4. Extracts data using configured CSS selectors
5. Writes results to `backend/data/prices.json` and copies to `frontend/public/data/prices.json`
6. Git commit triggers rebuild of static site

**Automation Strategy**
- GitHub Actions scheduled workflow runs daily at midnight UTC
- Executes scraper, commits updated JSON, triggers Netlify rebuild
- Zero server costs - everything runs on free tier services

### Content Strategy

**Blog System**
- Markdown files in `frontend/src/content/blog/`
- Shopping guides, buying advice, product comparisons
- SEO-focused with proper meta descriptions and dates
- Examples include laptop guides, smartphone comparisons, money-saving tips

**Site Configuration**
- Global constants in `frontend/src/consts.ts`
- Site title: "AutoCompare - Price Comparison & Shopping Guide"
- Consistent branding across all pages

### Styling Approach

**Minimal CSS Framework**
- Custom CSS in `frontend/src/styles/global.css`
- Based on Bear Blog's clean, minimal design
- CSS variables for theming (accent colors, grays, shadows)
- Atkinson font family for readability
- Responsive design with max-width constraints

## External Dependencies

### Core Technologies
- **Astro 5.15.4**: Static site generator framework
- **Python 3.11**: Scraper runtime
- **Playwright**: Headless browser automation library
- **Node.js 20+**: Build tooling and package management

### Astro Integrations
- **@astrojs/mdx**: Enhanced markdown with component support
- **@astrojs/rss**: Automatic RSS feed generation
- **@astrojs/sitemap**: SEO sitemap generation
- **sharp**: Image optimization

### Python Dependencies
- **playwright**: Browser automation
- **aiofiles**: Async file I/O operations

### Deployment & Hosting
- **Netlify**: Static site hosting (free tier)
  - Build command: `npm run build --prefix frontend`
  - Publish directory: `frontend/dist`
  - Custom domain support
  - CDN included
- **GitHub Actions**: Automation runner for scheduled scraping

### Development Tools
- **TypeScript**: Type checking for Astro components
- **Git**: Version control and data persistence

### Data Storage
- **File-based JSON**: No database required
  - `backend/configs/sites.json`: Scraper configuration
  - `backend/data/prices.json`: Raw scraped data
  - `frontend/public/data/prices.json`: Published price data
- **Git repository**: Acts as database and version history

### Browser
- **Chromium**: Installed via Playwright for scraping (headless mode)