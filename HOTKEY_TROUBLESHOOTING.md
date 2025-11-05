# Hotkey Troubleshooting Guide

## Issue: Ctrl+Shift+V doesn't open the clipboard manager

### Quick Fixes

#### Fix 1: Run the Diagnostic Tool

```bash
python3 diagnose_hotkey.py
```

This will test your hotkey setup and identify the problem.

#### Fix 2: Use the Button Version (Workaround)

If the hotkey doesn't work, use the version with a button:

```bash
python3 main_with_button.py
```

This creates a small window with a button to open the clipboard manager.

#### Fix 3: Change the Hotkey

Edit `~/.smart-clipboard/config.json`:

```json
{
  "hotkey": "<ctrl>+<alt>+v"
}
```

Try different combinations:
- `<ctrl>+<alt>+v`
- `<ctrl>+<alt>+c`
- `<alt>+<shift>+v`

Then restart the application.

---

## Platform-Specific Solutions

### Linux

#### Problem: Permission Issues

**Solution 1: Add user to input group**
```bash
sudo usermod -a -G input $USER
```
Then log out and log back in.

**Solution 2: Run with sudo (temporary)**
```bash
sudo python3 main.py
```

**Solution 3: Check X11 vs Wayland**
```bash
echo $XDG_SESSION_TYPE
```

If using Wayland, try switching to X11 session at login.

#### Problem: Another app is using the hotkey

Check what's using Ctrl+Shift+V:
```bash
xbindkeys --show
```

### Windows

#### Problem: Permission Issues

**Solution: Run as Administrator**
1. Right-click on Command Prompt
2. Select "Run as administrator"
3. Navigate to project folder
4. Run: `python main.py`

#### Problem: Another app is using the hotkey

Common culprits:
- Microsoft Teams
- Slack
- Discord
- Other clipboard managers

Close these apps or change their hotkeys.

### macOS

#### Problem: Accessibility Permissions

**Solution: Grant accessibility permissions**
1. Open System Preferences → Security & Privacy
2. Go to Privacy tab → Accessibility
3. Click the lock to make changes
4. Add Terminal or Python to the list
5. Restart the application

---

## Alternative Solutions

### Solution 1: Use the Button Version

```bash
python3 main_with_button.py
```

This creates a small control window with a button:

```
┌─────────────────────────────┐
│ Smart Clipboard Manager     │
│                             │
│  [Open Clipboard Manager]   │
│                             │
│  Monitoring clipboard...    │
└─────────────────────────────┘
```

Click the button to open the clipboard manager.

### Solution 2: Create a Desktop Shortcut

**Linux:**
Create `~/.local/share/applications/clipboard-manager.desktop`:
```ini
[Desktop Entry]
Name=Clipboard Manager
Exec=python3 /path/to/Project-tools/main_with_button.py
Icon=edit-paste
Type=Application
Categories=Utility;
```

**Windows:**
Create a shortcut with target:
```
pythonw.exe "C:\path\to\Project-tools\main_with_button.py"
```

**macOS:**
Use Automator to create an application.

### Solution 3: Use a Different Hotkey Library

If pynput doesn't work, we can switch to:
- `keyboard` library (requires root on Linux)
- `pyautogui` (different approach)
- Platform-specific solutions

---

## Testing Steps

### Step 1: Test pynput Installation

```bash
python3 -c "from pynput import keyboard; print('OK')"
```

Should print "OK". If not:
```bash
pip install --upgrade pynput
```

### Step 2: Test Basic Hotkey

```bash
python3 test_hotkey.py
```

Press Ctrl+Shift+V. Should print "✅ Hotkey detected!"

### Step 3: Test Full Application

```bash
python3 main.py
```

Press Ctrl+Shift+V. The clipboard manager window should appear.

---

## Common Error Messages

### "Error starting hotkey handler: ..."

**Cause**: Permission issues or conflicting applications

**Solution**:
1. Run diagnostic: `python3 diagnose_hotkey.py`
2. Try button version: `python3 main_with_button.py`
3. Change hotkey in config.json

### "No module named 'pynput'"

**Cause**: pynput not installed

**Solution**:
```bash
pip install pynput
```

### "Permission denied"

**Cause**: Insufficient permissions to monitor keyboard

**Solution** (Linux):
```bash
sudo usermod -a -G input $USER
```
Then log out and log back in.

---

## Debugging

### Enable Debug Mode

Edit `main.py` and add debug prints:

```python
def toggle_ui(self):
    print("DEBUG: toggle_ui called!")  # Add this
    if self.root.winfo_viewable():
        self.ui.hide()
    else:
        self.ui.show()
```

### Check if Hotkey Handler Started

Look for this message when starting:
```
✅ Hotkey handler started: <ctrl>+<shift>+v
```

If you see:
```
❌ Error starting hotkey handler: ...
```

Then there's a problem with the hotkey setup.

### Test Manually

Open Python and test:

```python
from pynput import keyboard

def on_activate():
    print("Hotkey pressed!")

with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+v': on_activate
}) as h:
    h.join()
```

Press Ctrl+Shift+V. Should print "Hotkey pressed!"

---

## Recommended Solutions

### Best: Use Button Version

Most reliable across all platforms:
```bash
python3 main_with_button.py
```

### Good: Change Hotkey

If Ctrl+Shift+V is taken, use Ctrl+Alt+V:

Edit `~/.smart-clipboard/config.json`:
```json
{
  "hotkey": "<ctrl>+<alt>+v"
}
```

### Alternative: Desktop Shortcut

Create a shortcut to open the clipboard manager with a single click.

---

## Still Not Working?

### Option 1: Report the Issue

Run the diagnostic and share the output:
```bash
python3 diagnose_hotkey.py > diagnostic.txt
```

### Option 2: Use Without Hotkey

The button version works perfectly without hotkeys:
```bash
python3 main_with_button.py
```

### Option 3: Manual Testing

Test each component separately:
1. Test hotkey: `python3 test_hotkey.py`
2. Test diagnostic: `python3 diagnose_hotkey.py`
3. Test UI: `python3 demo.py`

---

## Summary

| Problem | Solution |
|---------|----------|
| Hotkey not working | Use `main_with_button.py` |
| Permission denied | Add user to input group (Linux) |
| Another app using hotkey | Change hotkey in config.json |
| pynput not installed | `pip install pynput` |
| Need admin rights | Run with sudo/admin |

---

**The button version (`main_with_button.py`) is the most reliable solution and works on all platforms!**

