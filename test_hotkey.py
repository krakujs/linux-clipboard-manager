#!/usr/bin/env python3
"""
Test hotkey detection
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

print("Testing hotkey detection...")
print("Press Ctrl+Shift+V to test")
print("Press Ctrl+C to exit")
print("-" * 60)

try:
    from pynput import keyboard
    
    def on_activate():
        print("✅ Hotkey detected! Ctrl+Shift+V was pressed!")
    
    # Use pynput's GlobalHotKeys (the proper way)
    with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+v': on_activate
    }) as h:
        h.join()
        
except ImportError:
    print("❌ pynput not installed")
    print("Run: pip install pynput")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

