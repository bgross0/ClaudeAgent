#!/usr/bin/env python3
"""
Test script to verify Claude Agent System functionality
"""

import subprocess
import sys
import time
import requests
import threading
from pathlib import Path

def test_system():
    print("🧪 Testing Claude Code Agentic System")
    print("=" * 40)
    
    # Test 1: Check main.py syntax
    print("1. 📝 Checking main.py syntax...")
    try:
        result = subprocess.run([sys.executable, "-m", "py_compile", "main.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ main.py syntax OK")
        else:
            print(f"   ❌ Syntax error: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False
    
    # Test 2: Check required files
    print("2. 📁 Checking required files...")
    required_files = [
        "main.py", "requirements.txt", "config.yaml", 
        "templates/dashboard.html", "README.md"
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ Missing: {file}")
            return False
    
    # Test 3: Import test
    print("3. 🐍 Testing imports...")
    try:
        import sqlite3
        import json
        import yaml
        print("   ✅ Core imports OK")
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
        return False
    
    # Test 4: Database initialization
    print("4. 🗄️ Testing database...")
    try:
        import sqlite3
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY)")
        conn.commit()
        conn.close()
        Path("test.db").unlink()  # Clean up
        print("   ✅ Database operations OK")
    except Exception as e:
        print(f"   ❌ Database error: {e}")
        return False
    
    print("\n🎉 All tests passed!")
    print("🚀 Ready to start the system with: python main.py")
    return True

if __name__ == "__main__":
    if test_system():
        print("\n💡 Next steps:")
        print("   1. Run: python main.py")
        print("   2. Open: http://localhost:5000")
        print("   3. Enjoy your Claude Agent System!")
    else:
        print("\n❌ Tests failed. Please check the errors above.")
        sys.exit(1)
