#!/usr/bin/env python3
"""
Diagnostic script for hotkey issues
"""
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

print("="*60)
print("HOTKEY DIAGNOSTIC TOOL")
print("="*60)

# Check 1: Python version
print("\n1. Checking Python version...")
version = sys.version_info
print(f"   Python {version.major}.{version.minor}.{version.micro}")
if version.major >= 3 and version.minor >= 7:
    print("   ✅ Version OK")
else:
    print("   ❌ Need Python 3.7+")

# Check 2: pynput installation
print("\n2. Checking pynput installation...")
try:
    from pynput import keyboard
    print("   ✅ pynput is installed")
except ImportError:
    print("   ❌ pynput not installed")
    print("   Run: pip install pynput")
    sys.exit(1)

# Check 3: Permissions (Linux)
print("\n3. Checking permissions...")
if sys.platform.startswith('linux'):
    import getpass
    user = getpass.getuser()
    print(f"   Current user: {user}")
    
    # Check if user is in input group
    try:
        import grp
        input_group = grp.getgrnam('input')
        if user in input_group.gr_mem:
            print("   ✅ User is in 'input' group")
        else:
            print("   ⚠️  User is NOT in 'input' group")
            print("   This may cause permission issues")
            print("   Fix: sudo usermod -a -G input $USER")
            print("   Then log out and log back in")
    except KeyError:
        print("   ⚠️  'input' group not found")
else:
    print("   ✅ Not Linux, no special permissions needed")

# Check 4: Test basic keyboard listener
print("\n4. Testing basic keyboard listener...")
print("   Press any key (will timeout in 3 seconds)...")

key_pressed = False

def on_press(key):
    global key_pressed
    key_pressed = True
    print(f"   ✅ Key detected: {key}")
    return False  # Stop listener

try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join(timeout=3)
    
    if not key_pressed:
        print("   ⚠️  No key detected (timeout)")
        print("   This may indicate permission issues")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Check 5: Test GlobalHotKeys
print("\n5. Testing GlobalHotKeys (Ctrl+Shift+V)...")
print("   Press Ctrl+Shift+V (will timeout in 5 seconds)...")

hotkey_pressed = False

def on_activate():
    global hotkey_pressed
    hotkey_pressed = True
    print("   ✅ Hotkey detected! Ctrl+Shift+V works!")

try:
    with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+v': on_activate
    }) as h:
        h.join(timeout=5)
    
    if not hotkey_pressed:
        print("   ⚠️  Hotkey not detected (timeout)")
        print("   Possible causes:")
        print("   - Another application is capturing Ctrl+Shift+V")
        print("   - Permission issues (try running with sudo)")
        print("   - X11/Wayland compatibility issues")
except Exception as e:
    print(f"   ❌ Error: {e}")
    import traceback
    traceback.print_exc()

# Check 6: Display environment
print("\n6. Checking display environment...")
if 'DISPLAY' in os.environ:
    print(f"   DISPLAY: {os.environ['DISPLAY']}")
    print("   ✅ Display environment set")
else:
    print("   ⚠️  DISPLAY not set")
    print("   This may cause issues on Linux")

if 'WAYLAND_DISPLAY' in os.environ:
    print(f"   WAYLAND_DISPLAY: {os.environ['WAYLAND_DISPLAY']}")
    print("   ℹ️  Using Wayland (may have compatibility issues)")

# Summary
print("\n" + "="*60)
print("DIAGNOSTIC SUMMARY")
print("="*60)

if hotkey_pressed:
    print("\n✅ HOTKEY WORKS!")
    print("   Ctrl+Shift+V is functioning correctly.")
    print("   The issue may be with the application integration.")
else:
    print("\n⚠️  HOTKEY NOT WORKING")
    print("\nPossible solutions:")
    print("1. Try a different hotkey combination")
    print("2. Check if another app is using Ctrl+Shift+V")
    print("3. On Linux, add user to input group:")
    print("   sudo usermod -a -G input $USER")
    print("   Then log out and log back in")
    print("4. Try running with elevated privileges:")
    print("   sudo python3 main.py")
    print("5. Check for X11/Wayland compatibility issues")

print("\n" + "="*60)
print("\nTo test the full application:")
print("  python3 main.py")
print("\nTo change the hotkey, edit:")
print("  ~/.smart-clipboard/config.json")
print("  Change 'hotkey' to something like '<ctrl>+<alt>+v'")
print("="*60)

