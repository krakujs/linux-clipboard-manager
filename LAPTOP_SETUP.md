# Smart Clipboard Manager - Laptop Setup Guide

## 🚀 Quick Setup for Your Laptop

This guide will help you get the Smart Clipboard Manager running on your laptop with full GUI support.

---

## Step 1: Transfer Files to Your Laptop

### Option A: Download/Copy the Project Folder

Copy the entire `Project-tools` folder to your laptop, or download it if it's in a repository.

### Option B: Clone from Repository (if applicable)

```bash
git clone <repository-url>
cd smart-clipboard
```

---

## Step 2: Install Dependencies

### For Windows:

```bash
# Open Command Prompt or PowerShell
cd path\to\Project-tools

# Install Python dependencies
pip install -r requirements.txt

# Install Windows-specific dependencies
pip install pywin32 psutil
```

### For macOS:

```bash
# Open Terminal
cd path/to/Project-tools

# Install Python dependencies
pip install -r requirements.txt

# No additional dependencies needed for macOS
```

### For Linux (Ubuntu/Debian):

```bash
# Open Terminal
cd path/to/Project-tools

# Install system dependencies
sudo apt-get update
sudo apt-get install python3-tk python3-pip xdotool

# Install Python dependencies
pip install -r requirements.txt
```

### For Linux (Fedora/RHEL):

```bash
sudo dnf install python3-tkinter xdotool
pip install -r requirements.txt
```

---

## Step 3: Verify Installation

Run the verification script to make sure everything is installed correctly:

```bash
python3 verify_installation.py
```

You should see:
```
🎉 ALL CHECKS PASSED!
```

---

## Step 4: Run the Application

### Start the Clipboard Manager:

```bash
python3 main.py
```

You should see:
```
Starting Smart Clipboard Manager...
✅ Config loaded from: ~/.smart-clipboard/config.json
✅ Database: ~/.smart-clipboard/clipboard.db
✅ Content analyzer initialized
✅ Smart Clipboard Manager is ready!

Hotkey: <ctrl>+<shift>+v
Press Ctrl+Shift+V to open the clipboard manager
Press Ctrl+C to exit
```

### Open the Clipboard Manager:

Press **Ctrl+Shift+V** (or **Cmd+Shift+V** on macOS)

A window will appear showing your clipboard history!

---

## Step 5: Start Using It!

### Basic Usage:

1. **Copy anything** - It's automatically saved
2. **Press Ctrl+Shift+V** - Opens the clipboard manager
3. **Search** - Type to filter your clipboard history
4. **Select and press Enter** - Pastes the selected clip
5. **Mark favorites** - Click the Favorite button for important clips

### Keyboard Shortcuts:

- **Ctrl+Shift+V** - Toggle clipboard manager window
- **Enter** - Paste selected clip
- **Escape** - Close window
- **Double-click** - Paste selected clip

---

## Troubleshooting

### Issue: "No module named 'tkinter'"

**Windows:**
- Reinstall Python and make sure to check "tcl/tk and IDLE" during installation

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
- tkinter should be included with Python. If not, reinstall Python from python.org

### Issue: Hotkey not working

1. Check if another application is using Ctrl+Shift+V
2. Try changing the hotkey in `~/.smart-clipboard/config.json`:
   ```json
   {
     "hotkey": "<ctrl>+<alt>+v"
   }
   ```
3. Restart the application

### Issue: "Permission denied" on Linux

The application needs permission to monitor keyboard input:

```bash
# Add your user to the input group
sudo usermod -a -G input $USER

# Log out and log back in for changes to take effect
```

### Issue: Application won't start

1. Check Python version: `python3 --version` (needs 3.7+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check for error messages in the terminal
4. Run verification: `python3 verify_installation.py`

---

## Configuration

### Config File Location:

- **Windows:** `C:\Users\YourName\.smart-clipboard\config.json`
- **macOS:** `~/.smart-clipboard/config.json`
- **Linux:** `~/.smart-clipboard/config.json`

### Common Customizations:

```json
{
  "max_history": 1000,
  "hotkey": "<ctrl>+<shift>+v",
  "excluded_apps": ["KeePass", "1Password", "LastPass"],
  "ui": {
    "window_width": 600,
    "window_height": 400
  }
}
```

---

## Auto-Start on Boot (Optional)

### Windows:

1. Press `Win+R`, type `shell:startup`, press Enter
2. Create a shortcut to `main.py` in the Startup folder
3. Right-click the shortcut → Properties
4. Set Target to: `pythonw.exe "C:\path\to\Project-tools\main.py"`

### macOS:

1. Open System Preferences → Users & Groups → Login Items
2. Click the "+" button
3. Navigate to and select `main.py`
4. Or create a Launch Agent (see ARCHITECTURE.md for details)

### Linux (Ubuntu/GNOME):

1. Open "Startup Applications"
2. Click "Add"
3. Name: Smart Clipboard Manager
4. Command: `python3 /path/to/Project-tools/main.py`
5. Click "Add"

---

## Features Overview

### Content Detection:
- 🔗 URLs (with domain extraction)
- 📧 Email addresses
- 💻 Code (Python, JavaScript, Java, C++, Go, Rust, etc.)
- {} JSON
- 📝 Markdown
- 📁 File paths
- 🔢 Numbers
- 📄 Plain text

### Privacy Features:
- 🔒 Excludes password managers automatically
- 🛡️ Detects sensitive content (passwords, credit cards)
- 💾 Local storage only (no cloud sync by default)

### Search & Filter:
- 🔍 Full-text search across all history
- 🏷️ Filter by content type (URLs, Code, etc.)
- ⭐ Favorites for quick access
- 📊 Usage statistics

---

## Testing Before Daily Use

### Run the Demo:

```bash
python3 demo.py
```

This will test all components without affecting your real clipboard.

### Test the GUI:

1. Start the application: `python3 main.py`
2. Copy some text
3. Press Ctrl+Shift+V
4. You should see the copied text in the list
5. Select it and press Enter to paste

---

## Performance Tips

### For Better Performance:

1. **Reduce history size** if you have limited RAM:
   ```json
   {
     "max_history": 500
   }
   ```

2. **Increase monitor interval** to reduce CPU usage:
   ```json
   {
     "monitor_interval": 1.0
   }
   ```

3. **Exclude large content**:
   ```json
   {
     "max_content_size": 524288
   }
   ```

---

## Uninstallation

### To Remove:

1. Stop the application (Ctrl+C in terminal)
2. Remove auto-start entry (if configured)
3. Delete the project folder
4. Delete config and database:
   - Windows: `C:\Users\YourName\.smart-clipboard\`
   - macOS/Linux: `~/.smart-clipboard/`

---

## Getting Help

### Documentation:
- **README.md** - Full user guide
- **QUICKSTART.md** - Quick start guide
- **ARCHITECTURE.md** - Technical details
- **PROJECT_SUMMARY.md** - Project overview

### Common Issues:
- Check terminal output for error messages
- Run `python3 verify_installation.py`
- Review the Troubleshooting section above

---

## What's Next?

Once you have it running:

1. ✅ Use it for a day to get familiar
2. ✅ Customize the hotkey if needed
3. ✅ Mark your favorite clips
4. ✅ Explore the search functionality
5. ✅ Set up auto-start for convenience

---

## Quick Reference Card

```
╔════════════════════════════════════════════════════════╗
║  SMART CLIPBOARD MANAGER - QUICK REFERENCE            ║
╠════════════════════════════════════════════════════════╣
║  Start:        python3 main.py                        ║
║  Open:         Ctrl+Shift+V                           ║
║  Paste:        Enter or Double-click                  ║
║  Close:        Escape                                 ║
║  Search:       Just start typing                      ║
║  Favorite:     Click Favorite button                  ║
║  Config:       ~/.smart-clipboard/config.json         ║
╚════════════════════════════════════════════════════════╝
```

---

**Enjoy your Smart Clipboard Manager! 📋✨**

