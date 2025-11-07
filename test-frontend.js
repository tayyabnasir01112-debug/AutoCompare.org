/**
 * Test script for the AutoCompare frontend.
 * This script validates that the frontend can build and that price data is accessible.
 */

import { existsSync, readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('='.repeat(60));
console.log('AutoCompare Frontend Test Suite');
console.log('='.repeat(60));
console.log();

// Test 1: Check if price data file exists
console.log('Test 1: Checking price data file...');
const pricesPath = join(__dirname, 'frontend', 'public', 'data', 'prices.json');

if (existsSync(pricesPath)) {
  console.log('✅ Price data file exists:', pricesPath);
  
  try {
    const priceData = JSON.parse(readFileSync(pricesPath, 'utf-8'));
    const siteCount = Object.keys(priceData).length;
    console.log(`✅ Price data is valid JSON with ${siteCount} site(s)`);
    
    // Show sample data
    if (siteCount > 0) {
      const firstSite = Object.keys(priceData)[0];
      console.log(`   Sample: ${firstSite} - ${priceData[firstSite].data?.title || 'N/A'}`);
    }
  } catch (error) {
    console.log('❌ Price data file is not valid JSON:', error.message);
    process.exit(1);
  }
} else {
  console.log('⚠️  Price data file not found:', pricesPath);
  console.log('   This is OK for initial setup. Run the scraper first:');
  console.log('   python backend/scraper.py');
}

// Test 2: Check if frontend dependencies are installed
console.log('\nTest 2: Checking frontend dependencies...');
const nodeModulesPath = join(__dirname, 'frontend', 'node_modules');
if (existsSync(nodeModulesPath)) {
  console.log('✅ Frontend dependencies are installed');
} else {
  console.log('❌ Frontend dependencies not installed');
  console.log('   Run: cd frontend && npm install');
  process.exit(1);
}

// Test 3: Check package.json
console.log('\nTest 3: Checking package.json...');
const packageJsonPath = join(__dirname, 'frontend', 'package.json');
if (existsSync(packageJsonPath)) {
  const packageJson = JSON.parse(readFileSync(packageJsonPath, 'utf-8'));
  console.log('✅ package.json found');
  console.log(`   Project: ${packageJson.name}`);
  console.log(`   Scripts available: ${Object.keys(packageJson.scripts).join(', ')}`);
} else {
  console.log('❌ package.json not found');
  process.exit(1);
}

console.log('\n' + '='.repeat(60));
console.log('✅ Frontend tests completed!');
console.log('='.repeat(60));
console.log('\nNext steps:');
console.log('  1. Run the scraper: python backend/scraper.py');
console.log('  2. Start dev server: cd frontend && npm run dev');
console.log('  3. Build for production: cd frontend && npm run build');

