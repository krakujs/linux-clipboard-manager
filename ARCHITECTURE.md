# Smart Clipboard Manager - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Smart Clipboard Manager                   │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   System     │────▶│  Clipboard   │────▶│   Content    │
│  Clipboard   │     │   Monitor    │     │   Analyzer   │
└──────────────┘     └──────────────┘     └──────────────┘
                            │                      │
                            ▼                      ▼
                     ┌──────────────┐     ┌──────────────┐
                     │   Storage    │◀────│  App Detector│
                     │   (SQLite)   │     └──────────────┘
                     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │      UI      │
                     │  (Tkinter)   │
                     └──────────────┘
                            ▲
                            │
                     ┌──────────────┐
                     │   Hotkey     │
                     │   Handler    │
                     └──────────────┘
```

## Component Details

### 1. Clipboard Monitor (`clipboard_monitor.py`)

**Purpose**: Continuously monitors system clipboard for changes

**Key Classes**:
- `ClipboardMonitor`: Low-level clipboard polling
- `ClipboardManager`: High-level clipboard management
- `AppDetector`: Detects active application (platform-specific)

**Flow**:
1. Polls clipboard every 0.5 seconds (configurable)
2. Detects changes by comparing with last known content
3. Triggers callback when new content detected
4. Passes content to analyzer and storage

**Threading**: Runs in background daemon thread

### 2. Content Analyzer (`content_analyzer.py`)

**Purpose**: Analyzes and categorizes clipboard content

**Key Class**: `ContentAnalyzer`

**Detection Capabilities**:
- URLs (with domain extraction)
- Email addresses
- Code (with language detection)
- JSON
- Markdown
- File paths
- Numbers
- Sensitive content (passwords, credit cards)

**Output**: Returns dict with:
- `content_type`: Category of content
- `is_sensitive`: Boolean flag
- `metadata`: Additional extracted information

### 3. Storage Engine (`storage.py`)

**Purpose**: Persistent storage with SQLite

**Key Class**: `ClipboardStorage`

**Database Schema**:
```sql
clipboard_history:
  - id (PRIMARY KEY)
  - content_hash (UNIQUE)
  - content (TEXT)
  - content_type (TEXT)
  - app_name (TEXT)
  - timestamp (DATETIME)
  - is_favorite (INTEGER)
  - use_count (INTEGER)
  - metadata (TEXT/JSON)

clipboard_fts:
  - Full-text search virtual table
```

**Features**:
- Deduplication via content hashing
- Full-text search (FTS5)
- Automatic cleanup of old entries
- Favorite marking
- Usage tracking

### 4. User Interface (`ui.py`)

**Purpose**: Tkinter-based GUI for clipboard management

**Key Class**: `ClipboardUI`

**Components**:
- Search bar with real-time filtering
- Listbox showing clipboard history
- Preview pane for full content
- Filter buttons (All, URLs, Code, Favorites)
- Action buttons (Paste, Favorite, Delete, Stats)

**Keyboard Shortcuts**:
- Enter: Paste selected
- Escape: Close window
- Double-click: Paste selected

### 5. Hotkey Handler (`hotkey_handler.py`)

**Purpose**: Global keyboard shortcut handling

**Key Classes**:
- `HotkeyHandler`: Single hotkey listener
- `HotkeyManager`: Multiple hotkey management

**Implementation**:
- Uses `pynput` library
- Monitors key press/release events
- Supports modifier keys (Ctrl, Shift, Alt, Cmd)
- Thread-safe with locking

### 6. Configuration (`config.py`)

**Purpose**: Centralized configuration management

**Key Class**: `Config`

**Features**:
- JSON-based configuration
- Default values with user overrides
- Dot notation for nested access
- Auto-save on changes
- Platform-specific paths

**Location**: `~/.smart-clipboard/config.json`

## Data Flow

### Clipboard Copy Event

```
1. User copies text
   ↓
2. ClipboardMonitor detects change
   ↓
3. AppDetector identifies source app
   ↓
4. Check if app is excluded → [YES] → Stop
   ↓ [NO]
5. ContentAnalyzer analyzes content
   ↓
6. Check if sensitive → [YES] → Stop
   ↓ [NO]
7. ClipboardStorage saves to database
   ↓
8. Cleanup old entries if needed
```

### Clipboard Paste Event

```
1. User presses hotkey (Ctrl+Shift+V)
   ↓
2. HotkeyHandler triggers callback
   ↓
3. UI window shows/hides
   ↓
4. User searches/filters clips
   ↓
5. User selects clip
   ↓
6. Preview shows full content
   ↓
7. User presses Enter or Paste button
   ↓
8. Content copied to system clipboard
   ↓
9. UI window hides
```

## Threading Model

```
Main Thread:
  - UI event loop (Tkinter)
  - User interactions

Background Threads:
  - ClipboardMonitor (daemon)
  - HotkeyHandler (daemon)

Thread Safety:
  - SQLite connection (check_same_thread=False)
  - Locks for shared state
```

## Storage Architecture

### Database Location
- Default: `~/.smart-clipboard/clipboard.db`
- Configurable via config.json

### Indexing Strategy
- Primary index on `id`
- Unique index on `content_hash` (deduplication)
- Index on `timestamp` (fast recent queries)
- Index on `content_type` (filtering)
- FTS5 virtual table (full-text search)

### Cleanup Strategy
- Triggered after each save
- Keeps favorites + N most recent
- Configurable via `max_history`

## Security Considerations

### Privacy Protection
1. **App Exclusion**: Skips password managers
2. **Sensitive Detection**: Identifies passwords, credit cards
3. **Local Storage**: No cloud sync by default
4. **Encryption**: Optional (configurable)

### Sensitive Content Patterns
- Credit card numbers
- Password-like strings
- Keywords: password, secret, token, api_key

## Performance Optimization

### Memory Management
- Lazy loading of history
- Limited preview length
- Configurable max content size
- Automatic cleanup

### Search Performance
- FTS5 for fast full-text search
- Indexed queries
- Limited result sets

### Startup Time
- Background thread initialization
- Lazy UI creation
- Minimal initial load

## Platform-Specific Implementations

### Windows
- **Clipboard**: pyperclip (Win32 API)
- **App Detection**: win32gui + psutil
- **Hotkeys**: pynput

### macOS
- **Clipboard**: pyperclip (NSPasteboard)
- **App Detection**: AppleScript
- **Hotkeys**: pynput

### Linux
- **Clipboard**: pyperclip (X11)
- **App Detection**: xdotool
- **Hotkeys**: pynput

## Extension Points

### Adding New Content Types
1. Add detection pattern to `ContentAnalyzer`
2. Add metadata extraction logic
3. Update UI icons in `ClipboardUI._get_type_icon()`

### Adding New Features
1. Create new module in `src/`
2. Import in `main.py`
3. Initialize in `SmartClipboardApp.__init__()`
4. Add configuration options if needed

### Custom Storage Backends
1. Implement interface matching `ClipboardStorage`
2. Replace in `SmartClipboardApp.__init__()`

## Testing Strategy

### Unit Tests
- Content analyzer patterns
- Storage operations
- Configuration management

### Integration Tests
- Clipboard monitoring
- UI interactions
- Hotkey handling

### Manual Testing
- Cross-platform compatibility
- Performance under load
- Edge cases (large content, special characters)

## Future Enhancements

### Planned Features
- [ ] Cloud sync (optional)
- [ ] OCR for images
- [ ] Clipboard templates
- [ ] Team sharing
- [ ] Browser extension
- [ ] Mobile companion app
- [ ] Advanced search filters
- [ ] Export/import functionality
- [ ] Encryption at rest
- [ ] Auto-start on boot

### Technical Improvements
- [ ] Async I/O for better performance
- [ ] Plugin system for extensibility
- [ ] Better error handling and logging
- [ ] Comprehensive test suite
- [ ] CI/CD pipeline
- [ ] Installer/packager for distribution

## Dependencies

### Core
- `pyperclip`: Clipboard access
- `pynput`: Keyboard monitoring
- `sqlite3`: Built-in (storage)
- `tkinter`: Built-in (UI)

### Optional
- `pillow`: Image handling
- `cryptography`: Encryption
- `python-dateutil`: Date parsing

### Platform-Specific
- Windows: `pywin32`, `psutil`
- Linux: `xdotool` (system package)
- macOS: None (uses built-in tools)

## Performance Metrics

### Target Metrics
- Clipboard detection latency: < 500ms
- Search response time: < 100ms
- UI open time: < 200ms
- Memory usage: < 50MB
- Database size: ~1MB per 1000 clips

### Bottlenecks
- Full-text search on large databases
- UI rendering with many clips
- Large content storage

### Optimizations
- Limit search results
- Paginate history display
- Compress large content
- Index optimization

