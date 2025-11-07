#!/usr/bin/env python3
"""
Validation script for AutoCompare setup.
Checks if all dependencies and configurations are correct.
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.11+"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"[OK] Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"[FAIL] Python {version.major}.{version.minor}.{version.micro} (requires 3.11+)")
        return False

def check_python_packages():
    """Check if required Python packages are installed"""
    print("\nChecking Python packages...")
    required = ['playwright', 'aiofiles']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"[OK] {package}")
        except ImportError:
            print(f"[FAIL] {package} (not installed)")
            missing.append(package)
    
    if missing:
        print(f"\nInstall missing packages with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    return True

def check_playwright_browsers():
    """Check if Playwright browsers are installed"""
    print("\nChecking Playwright browsers...")
    try:
        result = subprocess.run(
            ['playwright', 'install', '--dry-run', 'chromium'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if 'chromium' in result.stdout.lower() and 'installed' in result.stdout.lower():
            print("[OK] Chromium browser is installed")
            return True
        else:
            print("[WARN] Chromium browser may not be installed")
            print("   Run: playwright install chromium")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("[WARN] Could not verify Playwright browsers")
        print("   Run: playwright install chromium")
        return False

def check_config_files():
    """Check if configuration files exist"""
    print("\nChecking configuration files...")
    project_root = Path(__file__).parent.absolute()
    
    config_file = project_root / 'backend' / 'configs' / 'sites.json'
    if config_file.exists():
        print(f"[OK] Configuration file exists: {config_file}")
        return True
    else:
        print(f"[WARN] Configuration file not found: {config_file}")
        print("   This is OK for initial setup, but you'll need to create it.")
        return False

def check_data_files():
    """Check if data files exist"""
    print("\nChecking data files...")
    project_root = Path(__file__).parent.absolute()
    
    prices_file = project_root / 'backend' / 'data' / 'prices.json'
    frontend_prices = project_root / 'frontend' / 'public' / 'data' / 'prices.json'
    
    backend_exists = prices_file.exists()
    frontend_exists = frontend_prices.exists()
    
    if backend_exists:
        print(f"[OK] Backend price data exists: {prices_file}")
    else:
        print(f"[WARN] Backend price data not found: {prices_file}")
        print("   Run the scraper to generate: python backend/scraper.py")
    
    if frontend_exists:
        print(f"[OK] Frontend price data exists: {frontend_prices}")
    else:
        print(f"[WARN] Frontend price data not found: {frontend_prices}")
        print("   Run the scraper to generate: python backend/scraper.py")
    
    return backend_exists or frontend_exists

def check_node_installation():
    """Check if Node.js is installed"""
    print("\nChecking Node.js installation...")
    try:
        result = subprocess.run(
            ['node', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"[OK] Node.js {version}")
            
            # Check if version is 20+
            major_version = int(version.lstrip('v').split('.')[0])
            if major_version >= 20:
                return True
            else:
                print(f"[WARN] Node.js version should be 20+ (found {major_version})")
                return False
        else:
            print("[FAIL] Node.js not found")
            return False
    except FileNotFoundError:
        print("[FAIL] Node.js not installed")
        return False
    except subprocess.TimeoutExpired:
        print("[WARN] Could not check Node.js version")
        return False

def check_frontend_dependencies():
    """Check if frontend dependencies are installed"""
    print("\nChecking frontend dependencies...")
    project_root = Path(__file__).parent.absolute()
    node_modules = project_root / 'frontend' / 'node_modules'
    
    if node_modules.exists():
        print("[OK] Frontend dependencies are installed")
        return True
    else:
        print("[WARN] Frontend dependencies not installed")
        print("   Run: cd frontend && npm install")
        return False

def main():
    """Run all validation checks"""
    print("=" * 60)
    print("AutoCompare Setup Validation")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Python Packages", check_python_packages),
        ("Playwright Browsers", check_playwright_browsers),
        ("Configuration Files", check_config_files),
        ("Data Files", check_data_files),
        ("Node.js Installation", check_node_installation),
        ("Frontend Dependencies", check_frontend_dependencies),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"[FAIL] Error checking {name}: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "[PASS]" if result else "[WARN/INFO]"
        print(f"{status}: {name}")
    
    print(f"\nPassed: {passed}/{total} checks")
    
    if passed == total:
        print("\n[SUCCESS] All checks passed! Your setup looks good.")
        return 0
    else:
        print("\n[INFO] Some checks failed or returned warnings.")
        print("   Review the messages above and fix any issues.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

