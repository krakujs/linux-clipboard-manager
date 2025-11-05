#!/usr/bin/env python3
"""
Installation verification script for Smart Clipboard Manager
Checks all dependencies and components
"""
import sys
import importlib
from pathlib import Path


def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"  ❌ Python {version.major}.{version.minor}.{version.micro} (requires 3.7+)")
        return False


def check_dependencies():
    """Check required dependencies"""
    print("\nChecking dependencies...")
    
    dependencies = {
        'pyperclip': 'Clipboard access',
        'pynput': 'Keyboard monitoring',
        'sqlite3': 'Database (built-in)',
        'json': 'JSON handling (built-in)',
        'threading': 'Threading (built-in)',
        'pathlib': 'Path handling (built-in)',
    }
    
    optional_deps = {
        'tkinter': 'GUI (built-in, requires display)',
        'PIL': 'Image handling (optional)',
        'cryptography': 'Encryption (optional)',
    }
    
    all_ok = True
    
    # Check required
    for module, description in dependencies.items():
        try:
            importlib.import_module(module)
            print(f"  ✅ {module:15} - {description}")
        except ImportError:
            print(f"  ❌ {module:15} - {description} (MISSING)")
            all_ok = False
    
    # Check optional
    print("\nOptional dependencies:")
    for module, description in optional_deps.items():
        try:
            importlib.import_module(module)
            print(f"  ✅ {module:15} - {description}")
        except ImportError:
            print(f"  ⚠️  {module:15} - {description} (not available)")
    
    return all_ok


def check_project_structure():
    """Check project files"""
    print("\nChecking project structure...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'src/__init__.py',
        'src/config.py',
        'src/storage.py',
        'src/content_analyzer.py',
        'src/clipboard_monitor.py',
        'src/hotkey_handler.py',
        'src/ui.py',
    ]
    
    all_ok = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (MISSING)")
            all_ok = False
    
    return all_ok


def check_components():
    """Check if components can be imported"""
    print("\nChecking components...")
    
    sys.path.insert(0, str(Path(__file__).parent))
    
    components = [
        ('src.config', 'Config'),
        ('src.storage', 'ClipboardStorage'),
        ('src.content_analyzer', 'ContentAnalyzer'),
        ('src.clipboard_monitor', 'ClipboardMonitor'),
        ('src.hotkey_handler', 'HotkeyHandler'),
    ]
    
    all_ok = True
    for module_name, class_name in components:
        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            print(f"  ✅ {module_name}.{class_name}")
        except Exception as e:
            print(f"  ❌ {module_name}.{class_name} - {e}")
            all_ok = False
    
    return all_ok


def test_basic_functionality():
    """Test basic functionality"""
    print("\nTesting basic functionality...")
    
    sys.path.insert(0, str(Path(__file__).parent))
    
    try:
        # Test content analyzer
        from src.content_analyzer import ContentAnalyzer
        analyzer = ContentAnalyzer()
        result = analyzer.analyze("https://example.com")
        assert result['content_type'] == 'url'
        print("  ✅ Content analyzer works")
        
        # Test storage
        from src.storage import ClipboardStorage
        storage = ClipboardStorage(":memory:")  # In-memory database
        clip_id = storage.save_clip("test content", "text")
        assert clip_id is not None
        storage.close()
        print("  ✅ Storage works")
        
        # Test config
        from src.config import Config
        config = Config()
        assert config.get('max_history') == 1000
        print("  ✅ Configuration works")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Functionality test failed: {e}")
        return False


def main():
    """Run all verification checks"""
    print("="*60)
    print("SMART CLIPBOARD MANAGER - INSTALLATION VERIFICATION")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Project Structure", check_project_structure),
        ("Components", check_components),
        ("Basic Functionality", test_basic_functionality),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} - {name}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 ALL CHECKS PASSED!")
        print("\nYour Smart Clipboard Manager is ready to use!")
        print("\nNext steps:")
        print("  1. Run the demo: python3 demo.py")
        print("  2. Run headless test: python3 test_headless.py")
        print("  3. Run the app (requires display): python3 main.py")
        print("  4. Press Ctrl+Shift+V to open clipboard manager")
        return 0
    else:
        print("\n⚠️  SOME CHECKS FAILED")
        print("\nPlease fix the issues above before running the application.")
        print("\nCommon fixes:")
        print("  - Install dependencies: pip install -r requirements.txt")
        print("  - For GUI support: install python3-tk package")
        return 1


if __name__ == "__main__":
    sys.exit(main())

