# Smart Clipboard Manager

A powerful clipboard manager with history, search, and smart categorization features.

## Features

### Core Features
- 📋 **Clipboard History**: Automatically saves your last 1000 clipboard entries
- 🔍 **Smart Search**: Full-text search across all clipboard history
- 🏷️ **Auto-Categorization**: Automatically detects URLs, emails, code, file paths, and more
- ⭐ **Favorites**: Pin frequently used clips for quick access
- 🔒 **Privacy Protection**: Automatically excludes sensitive content from password managers
- 🎯 **Deduplication**: Doesn't store identical content twice
- ⌨️ **Global Hotkey**: Quick access with Ctrl+Shift+V

### Content Types Detected
- 🔗 URLs
- 📧 Email addresses
- 💻 Code (with language detection)
- 📁 File paths
- 🔢 Numbers
- {} JSON
- 📝 Markdown
- 📄 Plain text

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Platform-Specific Dependencies

**Windows:**
```bash
pip install pywin32 psutil
```

**macOS:**
No additional dependencies needed (uses built-in AppleScript)

**Linux:**
```bash
sudo apt-get install xdotool  # For app detection
```

## Usage

### Starting the Application

```bash
python main.py
```

The application will start in the background and begin monitoring your clipboard.

### Opening the Clipboard Manager

Press **Ctrl+Shift+V** (or your configured hotkey) to open the clipboard manager window.

### Keyboard Shortcuts

- **Ctrl+Shift+V**: Toggle clipboard manager window
- **Enter**: Paste selected clip
- **Escape**: Close window
- **Double-click**: Paste selected clip

### Using the Interface

1. **Search**: Type in the search box to filter clipboard history
2. **Filter by Type**: Click buttons to filter by content type (All, URLs, Code, Favorites)
3. **Preview**: Click on any clip to see full content in preview pane
4. **Paste**: Select a clip and press Enter or click "Paste" button
5. **Favorite**: Mark clips as favorites for quick access
6. **Delete**: Remove unwanted clips from history
7. **Stats**: View statistics about your clipboard usage

## Configuration

Configuration file is located at: `~/.smart-clipboard/config.json`

### Default Configuration

```json
{
  "max_history": 1000,
  "monitor_interval": 0.5,
  "hotkey": "<ctrl>+<shift>+v",
  "database_path": "clipboard.db",
  "max_content_size": 1048576,
  "enable_encryption": false,
  "excluded_apps": ["KeePass", "1Password", "LastPass"],
  "categories": {
    "url": true,
    "email": true,
    "code": true,
    "image": true
  },
  "ui": {
    "max_preview_length": 100,
    "window_width": 600,
    "window_height": 400,
    "theme": "light"
  }
}
```

### Configuration Options

- **max_history**: Maximum number of clipboard entries to keep (default: 1000)
- **monitor_interval**: How often to check clipboard in seconds (default: 0.5)
- **hotkey**: Global hotkey combination (default: `<ctrl>+<shift>+v`)
- **database_path**: Path to SQLite database file
- **max_content_size**: Maximum size of clipboard content in bytes (default: 1MB)
- **enable_encryption**: Enable encryption for stored clipboard data (default: false)
- **excluded_apps**: List of applications to exclude from clipboard monitoring
- **categories**: Enable/disable content categorization
- **ui**: User interface settings

### Customizing the Hotkey

Edit the `hotkey` field in the config file. Examples:
- `<ctrl>+<shift>+v` (default)
- `<ctrl>+<alt>+c`
- `<cmd>+<shift>+v` (macOS)

## Project Structure

```
smart-clipboard/
├── src/
│   ├── __init__.py
│   ├── clipboard_monitor.py    # Background clipboard monitoring
│   ├── storage.py               # SQLite storage engine
│   ├── ui.py                    # Tkinter GUI interface
│   ├── hotkey_handler.py        # Global hotkey management
│   ├── content_analyzer.py      # Content categorization
│   └── config.py                # Configuration management
├── requirements.txt             # Python dependencies
├── main.py                      # Application entry point
└── README.md                    # This file
```

## Architecture

### Components

1. **ClipboardMonitor**: Background service that monitors clipboard changes
2. **ClipboardStorage**: SQLite-based storage with full-text search
3. **ContentAnalyzer**: Analyzes and categorizes clipboard content
4. **ClipboardUI**: Tkinter-based user interface
5. **HotkeyHandler**: Global keyboard shortcut handler
6. **Config**: Configuration management system

### Data Flow

```
Clipboard Change → Monitor → Analyzer → Storage → UI
                                ↓
                          App Detection
                          Privacy Check
                          Deduplication
```

## Privacy & Security

- **Excluded Apps**: Automatically excludes clipboard content from password managers
- **Sensitive Content Detection**: Detects and optionally excludes passwords, credit cards, etc.
- **Local Storage**: All data stored locally in SQLite database
- **No Cloud Sync**: By default, no data leaves your machine

## Troubleshooting

### Hotkey Not Working

- Check if another application is using the same hotkey
- Try changing the hotkey in config.json
- On Linux, ensure you have proper X11 permissions

### Clipboard Not Being Monitored

- Check if the application is running (`ps aux | grep main.py`)
- Verify clipboard access permissions
- Check console output for error messages

### High Memory Usage

- Reduce `max_history` in config.json
- Reduce `max_content_size` to exclude large clipboard items
- Run cleanup: The app automatically removes old entries

## Development

### Running Tests

```bash
pytest tests/
```

### Adding New Features

1. Create new module in `src/`
2. Import and integrate in `main.py`
3. Update configuration if needed
4. Add tests in `tests/`

## Future Enhancements

- [ ] Cloud sync across devices
- [ ] OCR for images
- [ ] Clipboard templates
- [ ] Team sharing features
- [ ] Browser extension
- [ ] Mobile app
- [ ] Encryption at rest
- [ ] Advanced search filters
- [ ] Export/import functionality

## License

MIT License - Feel free to use and modify!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the project repository.

---

**Made with ❤️ for productivity enthusiasts**

