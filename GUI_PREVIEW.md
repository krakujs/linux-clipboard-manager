# Smart Clipboard Manager - GUI Preview

## 🖥️ What the GUI Looks Like

### Main Window

```
╔═══════════════════════════════════════════════════════════════╗
║  Smart Clipboard Manager                                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Search: [_____________________________]                      ║
║          [All] [URLs] [Code] [⭐]                             ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  Clipboard History:                                           ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ ⭐ 🔗 https://github.com/user/awesome-project          │ ║
║  │    📧 contact@example.com                              │ ║
║  │    💻 def calculate_sum(a, b): return a + b            │ ║
║  │    {} {"name": "Smart Clipboard", "version": "1.0"}    │ ║
║  │    📄 Remember to buy: milk, eggs, bread, coffee       │ ║
║  │    🔗 https://stackoverflow.com/questions/12345        │ ║
║  │    📧 admin@company.com                                │ ║
║  │    📄 SELECT * FROM users WHERE active = 1;            │ ║
║  │    📄 TODO: Finish the clipboard manager project       │ ║
║  │    📄 pip install smart-clipboard-manager              │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  Preview:                                                     ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ https://github.com/user/awesome-project                 │ ║
║  │                                                          │ ║
║  │ This is the full content of the selected clipboard      │ ║
║  │ entry. You can see the complete text here before        │ ║
║  │ pasting it.                                             │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  [Paste] [Favorite] [Delete] [Stats]              [Close]    ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎨 UI Components

### 1. Search Bar
- **Type to search** - Filters clipboard history in real-time
- **Full-text search** - Searches across all clipboard content
- **Instant results** - Updates as you type

### 2. Filter Buttons
- **All** - Show all clipboard entries
- **URLs** - Show only URLs (🔗)
- **Code** - Show only code snippets (💻)
- **⭐** - Show only favorites

### 3. Clipboard History List
- **Icons** - Visual indicators for content type
  - 🔗 URLs
  - 📧 Emails
  - 💻 Code
  - {} JSON
  - 📝 Markdown
  - 📄 Text
  - 📁 File paths
  - 🔢 Numbers
- **⭐ Favorites** - Starred items appear first
- **Scrollable** - Shows up to 100 recent items
- **Click to select** - Preview appears below

### 4. Preview Pane
- **Full content** - See complete text before pasting
- **Scrollable** - For long content
- **Read-only** - Safe preview without editing

### 5. Action Buttons
- **Paste** - Copy to clipboard and close window
- **Favorite** - Toggle favorite status (⭐)
- **Delete** - Remove from history
- **Stats** - View usage statistics
- **Close** - Hide window (Escape key)

---

## ⌨️ Keyboard Shortcuts

### Global Shortcuts
- **Ctrl+Shift+V** - Open/close clipboard manager
- **Cmd+Shift+V** - On macOS

### Window Shortcuts
- **Enter** - Paste selected clip
- **Escape** - Close window
- **↑/↓ Arrow keys** - Navigate list
- **Type** - Start searching

### Mouse Actions
- **Single click** - Select and preview
- **Double click** - Paste and close
- **Right click** - Context menu (future feature)

---

## 🎯 Usage Scenarios

### Scenario 1: Quick Paste from History

```
1. Copy something: "https://github.com/user/repo"
2. Copy something else: "contact@example.com"
3. Press Ctrl+Shift+V
4. Select the URL from history
5. Press Enter
6. URL is pasted!
```

### Scenario 2: Search for Old Clipboard

```
1. Press Ctrl+Shift+V
2. Type "github" in search box
3. See all GitHub URLs you've copied
4. Select one and press Enter
5. Done!
```

### Scenario 3: Organize with Favorites

```
1. Press Ctrl+Shift+V
2. Select your email signature
3. Click "Favorite" button
4. Now it's always at the top with ⭐
5. Quick access anytime!
```

### Scenario 4: Filter by Type

```
1. Press Ctrl+Shift+V
2. Click "Code" button
3. See only code snippets you've copied
4. Select and paste
```

---

## 📊 Statistics Window

When you click "Stats", you'll see:

```
╔═══════════════════════════════════════╗
║  Statistics                           ║
╠═══════════════════════════════════════╣
║  Total clips: 150                     ║
║  Favorites: 5                         ║
║                                       ║
║  By type:                             ║
║    🔗 url: 45                         ║
║    📧 email: 12                       ║
║    💻 code: 38                        ║
║    {} json: 8                         ║
║    📄 text: 47                        ║
║                                       ║
║           [OK]                        ║
╚═══════════════════════════════════════╝
```

---

## 🎨 Visual Features

### Content Type Icons

| Icon | Type | Example |
|------|------|---------|
| 🔗 | URL | https://example.com |
| 📧 | Email | user@example.com |
| 💻 | Code | def hello(): pass |
| {} | JSON | {"key": "value"} |
| 📝 | Markdown | # Header |
| 📄 | Text | Plain text |
| 📁 | File Path | /home/user/file.txt |
| 🔢 | Number | 1234567890 |

### Favorite Indicator

```
⭐ 🔗 https://github.com/user/repo    ← Favorite
   📧 contact@example.com             ← Regular
```

### Preview Truncation

Long content is truncated in the list:
```
📄 This is a very long text that will be truncated in the list view...
```

But shown in full in the preview pane:
```
Preview:
┌─────────────────────────────────────┐
│ This is a very long text that will  │
│ be truncated in the list view but   │
│ you can see the full content here   │
│ in the preview pane before pasting  │
│ it to your application.             │
└─────────────────────────────────────┘
```

---

## 🔄 Real-Time Updates

The clipboard manager updates in real-time:

1. **Copy something** → Immediately appears in history
2. **Search** → Results update as you type
3. **Filter** → List updates instantly
4. **Favorite** → Star appears immediately

---

## 🎭 Window Behavior

### Opening
- **Appears centered** on screen
- **Focuses search box** automatically
- **Shows recent history** by default

### Closing
- **Escape key** - Quick close
- **Close button** - Click to close
- **After pasting** - Auto-closes

### Positioning
- **Remembers size** from config
- **Always on top** when open
- **Doesn't minimize** to taskbar

---

## 🌈 Theme (Future Enhancement)

Current: Light theme
Future: Dark theme option in config

```json
{
  "ui": {
    "theme": "dark"
  }
}
```

---

## 📱 Responsive Design

The window adapts to your screen:

- **Default**: 600x400 pixels
- **Configurable** in config.json
- **Minimum**: 400x300 pixels
- **Maximum**: Your screen size

---

## 🎯 Design Philosophy

### Simple & Clean
- No clutter
- Clear visual hierarchy
- Intuitive layout

### Fast & Efficient
- Keyboard-first design
- Quick access (Ctrl+Shift+V)
- Instant search

### Informative
- Content type icons
- Preview before paste
- Usage statistics

---

## 🚀 Getting Started

1. **Run**: `python3 main.py`
2. **Copy something**: Try copying this URL: https://github.com
3. **Open**: Press Ctrl+Shift+V
4. **See it**: Your copied URL appears in the list!
5. **Paste**: Select it and press Enter

---

## 💡 Pro Tips

1. **Use search** - Faster than scrolling
2. **Mark favorites** - For frequently used text
3. **Double-click** - Fastest way to paste
4. **Check preview** - Before pasting long content
5. **Use filters** - To find specific content types

---

**The GUI is ready and waiting for you on your laptop! 🎉**

