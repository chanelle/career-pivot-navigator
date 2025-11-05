#!/usr/bin/env python3
"""
Quick smoke test to verify Career Pivot Navigator setup
"""

import os
import sys
from pathlib import Path

def test_setup():
    """Run basic setup validation checks."""
    
    print("🔍 Career Pivot Navigator - Setup Verification\n")
    print("=" * 60)
    
    checks_passed = 0
    checks_failed = 0
    
    # Check 1: Python version
    print("\n1. Python Version Check...")
    python_version = sys.version_info
    if python_version >= (3, 8):
        print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
        checks_passed += 1
    else:
        print(f"   ❌ Python {python_version.major}.{python_version.minor} (need 3.8+)")
        checks_failed += 1
    
    # Check 2: Required imports
    print("\n2. Checking Python packages...")
    required_packages = [
        "langchain",
        "langchain_openai",
        "langchain_core",
        "dotenv",
        "streamlit",
        "openai",
        "pydantic"
    ]
    
    for package in required_packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            else:
                __import__(package)
            print(f"   ✅ {package}")
            checks_passed += 1
        except ImportError:
            print(f"   ❌ {package} (run: pip install -r requirements.txt)")
            checks_failed += 1
    
    # Check 3: OpenAI API Key
    print("\n3. Checking OpenAI API Key...")
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key.startswith("sk-"):
        print(f"   ✅ API key found (starts with: {api_key[:10]}...)")
        checks_passed += 1
    else:
        print("   ❌ API key not found or invalid")
        print("      → Edit .env file and set: OPENAI_API_KEY=sk-your-key")
        checks_failed += 1
    
    # Check 4: Project files
    print("\n4. Checking project files...")
    required_files = [
        "main.py",
        "analyze.py",
        "plan_generator.py",
        "prompts.py",
        "utils.py"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
            checks_passed += 1
        else:
            print(f"   ❌ {file} not found")
            checks_failed += 1
    
    # Check 5: Career map data
    print("\n5. Checking career_map.json...")
    career_map_paths = [
        "career_map.json",
        "../Data and Infrastructure/career_map.json"
    ]
    
    career_map_found = False
    for path in career_map_paths:
        if os.path.exists(path):
            print(f"   ✅ Found at: {path}")
            checks_passed += 1
            career_map_found = True
            break
    
    if not career_map_found:
        print("   ❌ career_map.json not found")
        checks_failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n📊 Results: {checks_passed} passed, {checks_failed} failed\n")
    
    if checks_failed == 0:
        print("✅ All checks passed! You're ready to run:")
        print("   python main.py              # CLI mode")
        print("   python main.py streamlit    # Web interface")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nQuick fixes:")
        print("• Install packages: pip install -r '../Data and Infrastructure/requirements.txt'")
        print("• Set API key in .env file")
        print("• Make sure you're in the 'Core Logic' directory")
    
    print()
    return checks_failed == 0

if __name__ == "__main__":
    success = test_setup()
    sys.exit(0 if success else 1)
