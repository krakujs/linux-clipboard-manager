# Smart Clipboard Manager - Deployment Guide

## 🚀 Installation Options

### Option 1: Automated System Installation (Recommended)

Run the automated installation script for a complete system-wide setup:

```bash
# Clone or download the project
git clone https://github.com/your-username/smart-clipboard-manager.git
cd smart-clipboard-manager

# Run the installation script
./install-system.sh
```

This will:
- Install all system dependencies
- Install Python packages
- Set up systemd user service
- Create desktop entry for application launcher
- Configure auto-start on login

### Option 2: Pip Installation

Install via pip for user-level installation:

```bash
# Install from local directory
pip install -e .

# Or install from remote repository (when published)
pip install smart-clipboard-manager
```

After pip installation, you'll need to manually set up the background service:

```bash
# Create systemd service
mkdir -p ~/.config/systemd/user/
cp smart-clipboard.service ~/.config/systemd/user/

# Enable and start service
systemctl --user daemon-reload
systemctl --user enable smart-clipboard.service
systemctl --user start smart-clipboard.service
```

### Option 3: Manual Installation

1. Install dependencies:
   ```bash
   sudo apt install python3 python3-pip python3-venv python3-full sqlite3 xdotool
   pip install --user -r requirements.txt
   ```

2. Run the application:
   ```bash
   python3 main.py
   ```

## 🎯 Usage

### After System Installation

- **Hotkey**: Press `Ctrl+Shift+V` to open the clipboard manager
- **Manual start**: Run `smart-clipboard-gui` from terminal
- **Service management**: 
  - Check status: `systemctl --user status smart-clipboard.service`
  - Stop service: `systemctl --user stop smart-clipboard.service`
  - Restart service: `systemctl --user restart smart-clipboard.service`

### After Pip Installation

- **Start background service**: `smart-clipboard`
- **Open GUI**: `smart-clipboard-gui`

## 📁 File Locations

### System Installation
- **Application**: `/usr/local/lib/smart-clipboard/`
- **Executables**: `/usr/local/bin/smart-clipboard*`
- **Service**: `~/.config/systemd/user/smart-clipboard.service`
- **Desktop entry**: `~/.local/share/applications/smart-clipboard.desktop`
- **Config**: `~/.smart-clipboard/config.json`
- **Database**: `~/.smart-clipboard/clipboard.db`

### User Installation
- **Config**: `~/.smart-clipboard/config.json`
- **Database**: `~/.smart-clipboard/clipboard.db`

## 🔧 Configuration

Edit the configuration file at `~/.smart-clipboard/config.json`:

```json
{
  "max_history": 1000,
  "monitor_interval": 0.5,
  "hotkey": "<ctrl>+<shift>+v",
  "ui": {
    "window_width": 600,
    "window_height": 400
  }
}
```

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

### Pip Installation
```bash
pip uninstall smart-clipboard-manager
rm -rf ~/.smart-clipboard/
```

## 🐛 Troubleshooting

### Service not starting
```bash
# Check service logs
journalctl --user -u smart-clipboard.service -f

# Check if dependencies are missing
python3 -c "import pyperclip, pynput; print('Dependencies OK')"
```

### Hotkey not working
- Check if another application is using the same hotkey
- Try changing the hotkey in config.json
- On Linux, ensure X11 permissions are properly set

### High memory usage
- Reduce `max_history` in config.json
- Reduce `max_content_size` to exclude large clipboard items

## 🔄 Updates

### System Installation
```bash
cd smart-clipboard-manager
git pull
./install-system.sh
```

### Pip Installation
```bash
pip install --upgrade smart-clipboard-manager
```
