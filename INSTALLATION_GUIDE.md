# 🚀 Smart Clipboard Manager - Installation Guide

## 📋 Quick Start

### One-Command Installation (Recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/your-username/smart-clipboard-manager/main/install-system.sh | bash
```

That's it! The clipboard manager will be installed and running automatically.

---

## 🔧 Alternative Installation Methods

### Method 1: pip Installation

```bash
# Install from PyPI
pip install smart-clipboard-manager

# Or install from source
pip install git+https://github.com/your-username/smart-clipboard-manager.git
```

### Method 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/your-username/smart-clipboard-manager.git
cd smart-clipboard-manager

# Run the installation script
./install-system.sh
```

### Method 3: Development Installation

```bash
# Clone and install in development mode
git clone https://github.com/your-username/smart-clipboard-manager.git
cd smart-clipboard-manager
pip install -e .
```

---

## ✅ Verification

After installation, verify everything is working:

### Check Service Status
```bash
systemctl --user status smart-clipboard.service
```

### Test the Application
1. Press `Ctrl+Shift+V` to open the clipboard manager
2. Copy some text to your clipboard
3. The new items should appear automatically in the manager

### Command Line Test
```bash
# Open GUI manually
smart-clipboard-gui

# Check if commands are available
which smart-clipboard
which smart-clipboard-gui
```

---

## 🎯 Usage Instructions

### Basic Usage

1. **Start**: The application starts automatically in the background
2. **Open UI**: Press `Ctrl+Shift+V` to open the clipboard manager
3. **Copy Items**: Click on any item to copy it to your clipboard
4. **Search**: Type in the search box to filter clipboard history
5. **Filter**: Use buttons to filter by content type (URLs, Code, Favorites)

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+V` | Toggle clipboard manager |
| `Enter` | Paste selected item |
| `Escape` | Close window |
| `Double-click` | Paste selected item |

### Command Line Commands

```bash
# Start background service
smart-clipboard

# Open GUI manually
smart-clipboard-gui

# Service management
systemctl --user status smart-clipboard.service
systemctl --user restart smart-clipboard.service
systemctl --user stop smart-clipboard.service
```

---

## ⚙️ Configuration

### Configuration File Location
`~/.smart-clipboard/config.json`

### Common Configuration Options

```json
{
  "hotkey": "<ctrl>+<shift>+v",
  "max_history": 1000,
  "ui": {
    "window_width": 600,
    "window_height": 400
  }
}
```

### Changing Hotkey
Edit the `hotkey` field in `config.json`:
- `<ctrl>+<shift>+v` (default)
- `<ctrl>+<alt>+c`
- `<cmd>+<shift>+v` (macOS)

---

## 🗂️ File Locations

### System Installation
- **Application**: `/usr/local/lib/smart-clipboard/`
- **Executables**: `/usr/local/bin/smart-clipboard*`
- **Service**: `~/.config/systemd/user/smart-clipboard.service`
- **Desktop Entry**: `~/.local/share/applications/smart-clipboard.desktop`
- **Config**: `~/.smart-clipboard/config.json`
- **Database**: `~/.smart-clipboard/clipboard.db`

### User Installation
- **Config**: `~/.smart-clipboard/config.json`
- **Database**: `~/.smart-clipboard/clipboard.db`

---

## 🔧 Troubleshooting

### Common Issues

#### Service Not Starting
```bash
# Check service logs
journalctl --user -u smart-clipboard.service -f

# Restart service
systemctl --user restart smart-clipboard.service
```

#### Hotkey Not Working
1. Check if another application uses the same hotkey
2. Try changing the hotkey in config.json
3. Ensure X11 permissions are properly set (Linux)

#### High Memory Usage
1. Reduce `max_history` in config.json
2. Reduce `max_content_size` to exclude large items

#### Permission Issues
```bash
# Fix file permissions
chmod +x /usr/local/bin/smart-clipboard*
chmod 644 ~/.config/systemd/user/smart-clipboard.service
```

### Getting Help

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/your-username/smart-clipboard-manager/issues)
- 💡 **Feature Requests**: [GitHub Issues](https://github.com/your-username/smart-clipboard-manager/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-username/smart-clipboard-manager/discussions)

---

## 🔄 Updates

### Automatic Updates (System Installation)
```bash
cd smart-clipboard-manager
git pull
./install-system.sh
```

### pip Updates
```bash
pip install --upgrade smart-clipboard-manager
```

### Development Updates
```bash
git pull
pip install -e .
```

---

## 🗑️ Uninstallation

### System Installation
```bash
# Stop and disable service
systemctl --user stop smart-clipboard.service
systemctl --user disable smart-clipboard.service

# Remove files
sudo rm -rf /usr/local/lib/smart-clipboard/
sudo rm -f /usr/local/bin/smart-clipboard*
rm -f ~/.config/systemd/user/smart-clipboard.service
rm -f ~/.local/share/applications/smart-clipboard.desktop

# Remove user data (optional)
rm -rf ~/.smart-clipboard/
```

### pip Installation
```bash
pip uninstall smart-clipboard-manager
rm -rf ~/.smart-clipboard/
```

---

## 📦 System Requirements

### Linux
- Python 3.7 or higher
- pip (Python package manager)
- System dependencies:
  ```bash
  sudo apt install python3 python3-pip python3-venv python3-full sqlite3 xdotool
  ```

### Other Platforms
- **Windows**: Additional `pywin32` and `psutil` packages required
- **macOS**: No additional dependencies needed

---

## 🎉 Installation Complete!

Your Smart Clipboard Manager is now installed and ready to use!

**Next Steps:**
1. ✅ Press `Ctrl+Shift+V` to open the clipboard manager
2. ✅ Copy some text and watch it appear automatically
3. ✅ Try the search and filtering features
4. ✅ Customize the configuration to your preferences

**Enjoy your enhanced clipboard experience!** 🚀
