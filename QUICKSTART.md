# Quick Start Guide

## Installation (3 steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

Or use the install script:
```bash
chmod +x install.sh
./install.sh
```

### 2. Test the Components
```bash
python3 demo.py
```

### 3. Run the Application
```bash
python3 main.py
```

Or use the run script:
```bash
chmod +x run.sh
./run.sh
```

## First Time Setup

When you first run the application:

1. **The app starts in the background** - You'll see a message in the terminal
2. **Press Ctrl+Shift+V** to open the clipboard manager window
3. **Start copying things** - Everything you copy will be saved automatically

## Basic Usage

### Opening the Clipboard Manager
- Press **Ctrl+Shift+V** (default hotkey)
- The window will appear with your clipboard history

### Searching
- Type in the search box to filter your clipboard history
- Search works across all clipboard content

### Pasting from History
1. Select a clip from the list
2. Press **Enter** or click **Paste**
3. The content is copied to your clipboard
4. The window closes automatically

### Keyboard Shortcuts
- **Ctrl+Shift+V** - Toggle clipboard manager
- **Enter** - Paste selected clip
- **Escape** - Close window
- **Double-click** - Paste selected clip

### Filtering
- **All** - Show all clips
- **URLs** - Show only URLs
- **Code** - Show only code snippets
- **⭐** - Show favorites

### Managing Clips
- **Favorite** - Mark important clips (they won't be auto-deleted)
- **Delete** - Remove unwanted clips
- **Stats** - View clipboard usage statistics

## Configuration

Config file location: `~/.smart-clipboard/config.json`

### Common Customizations

**Change the hotkey:**
```json
{
  "hotkey": "<ctrl>+<alt>+v"
}
```

**Increase history size:**
```json
{
  "max_history": 5000
}
```

**Exclude more apps:**
```json
{
  "excluded_apps": ["KeePass", "1Password", "LastPass", "Bitwarden"]
}
```

## Troubleshooting

### App won't start
```bash
# Check if dependencies are installed
pip list | grep -E "pyperclip|pynput"

# Reinstall dependencies
pip install -r requirements.txt
```

### Hotkey not working
1. Check if another app is using the same hotkey
2. Try a different hotkey in config.json
3. Restart the application

### Clipboard not being monitored
1. Make sure the app is running (check terminal)
2. Try copying something new
3. Check terminal for error messages

## Platform-Specific Notes

### Linux
- Install xdotool for app detection: `sudo apt-get install xdotool`
- May need X11 permissions for global hotkeys

### macOS
- Grant accessibility permissions when prompted
- Uses AppleScript for app detection

### Windows
- Install additional dependencies: `pip install pywin32 psutil`
- May need to run as administrator for global hotkeys

## Tips & Tricks

1. **Use favorites** for frequently used snippets (email signatures, code templates, etc.)
2. **Search by type** - Type "url:" to find all URLs
3. **Preview before pasting** - Click on a clip to see full content
4. **Clean up regularly** - Delete sensitive or outdated clips
5. **Check stats** - See what types of content you copy most

## Next Steps

- Customize your configuration in `~/.smart-clipboard/config.json`
- Set up auto-start on boot (platform-specific)
- Explore the codebase to add custom features
- Check out the full README.md for advanced features

## Getting Help

- Check the full README.md for detailed documentation
- Run `python3 demo.py` to test components
- Check terminal output for error messages
- Review the configuration file for available options

---

**Happy clipboard managing! 📋✨**

