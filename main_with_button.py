#!/usr/bin/env python3
"""
Smart Clipboard Manager - Alternative launcher with button
Use this if the hotkey doesn't work
"""
import sys
import signal
import tkinter as tk
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import Config
from src.storage import ClipboardStorage
from src.content_analyzer import ContentAnalyzer
from src.clipboard_monitor import ClipboardManager
from src.ui import ClipboardUI
from src.hotkey_handler import HotkeyHandler


class SmartClipboardAppWithButton:
    """Main application with a button to open clipboard manager"""
    
    def __init__(self):
        """Initialize the application"""
        print("Starting Smart Clipboard Manager (with button)...")
        
        # Initialize components
        self.config = Config()
        print(f"Config loaded from: {self.config.config_path}")
        
        db_path = self.config.get_database_path()
        self.storage = ClipboardStorage(str(db_path))
        print(f"Database: {db_path}")
        
        self.analyzer = ContentAnalyzer()
        
        self.clipboard_manager = ClipboardManager(
            self.storage,
            self.analyzer,
            self.config
        )
        
        self.ui = ClipboardUI(
            self.storage,
            self.analyzer,
            self.clipboard_manager,
            self.config
        )
        
        # Create UI window
        self.root = self.ui.create_window()
        
        # Create control button window
        self.create_control_window()
        
        # Setup hotkey (will try, but may not work)
        hotkey = self.config.get('hotkey', '<ctrl>+<shift>+v')
        try:
            self.hotkey_handler = HotkeyHandler(
                callback=self.toggle_ui,
                hotkey=hotkey
            )
            print(f"Hotkey: {hotkey}")
        except Exception as e:
            print(f"⚠️  Hotkey setup failed: {e}")
            self.hotkey_handler = None
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        print("Smart Clipboard Manager is ready!")
        print("Click the 'Open Clipboard Manager' button to access your history")
        if self.hotkey_handler:
            print("Or press Ctrl+Shift+V")
    
    def create_control_window(self):
        """Create a small control window with button"""
        self.control_window = tk.Toplevel(self.root)
        self.control_window.title("Clipboard Manager Control")
        self.control_window.geometry("300x150")
        
        # Center the window
        self.control_window.update_idletasks()
        width = self.control_window.winfo_width()
        height = self.control_window.winfo_height()
        x = (self.control_window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.control_window.winfo_screenheight() // 2) - (height // 2)
        self.control_window.geometry(f'{width}x{height}+{x}+{y}')
        
        # Make it stay on top
        self.control_window.attributes('-topmost', True)
        
        # Content
        frame = tk.Frame(self.control_window, padx=20, pady=20)
        frame.pack(expand=True, fill='both')
        
        label = tk.Label(
            frame,
            text="Smart Clipboard Manager",
            font=('Arial', 12, 'bold')
        )
        label.pack(pady=10)
        
        button = tk.Button(
            frame,
            text="📋 Open Clipboard Manager",
            command=self.show_ui,
            font=('Arial', 10),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        button.pack(pady=10)
        
        status_label = tk.Label(
            frame,
            text="Monitoring clipboard...",
            font=('Arial', 9),
            fg='gray'
        )
        status_label.pack(pady=5)
        
        # Handle window close
        self.control_window.protocol("WM_DELETE_WINDOW", self.on_control_close)
    
    def show_ui(self):
        """Show the clipboard manager UI"""
        self.ui.show()
    
    def toggle_ui(self):
        """Toggle UI visibility"""
        if self.root.winfo_viewable():
            self.ui.hide()
        else:
            self.ui.show()
    
    def on_control_close(self):
        """Handle control window close"""
        if tk.messagebox.askokcancel("Quit", "Stop clipboard monitoring?"):
            self.stop()
    
    def start(self):
        """Start the application"""
        # Start clipboard monitoring
        self.clipboard_manager.start()
        
        # Start hotkey handler if available
        if self.hotkey_handler:
            self.hotkey_handler.start()
        
        # Start UI event loop
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nShutting down...")
            self.stop()
    
    def stop(self):
        """Stop the application"""
        print("Stopping Smart Clipboard Manager...")
        
        # Stop hotkey handler
        if self.hotkey_handler:
            self.hotkey_handler.stop()
        
        # Stop clipboard monitoring
        self.clipboard_manager.stop()
        
        # Close storage
        self.storage.close()
        
        # Close windows
        try:
            self.control_window.destroy()
        except:
            pass
        
        try:
            self.root.destroy()
        except:
            pass
        
        print("Goodbye!")
        sys.exit(0)
    
    def _signal_handler(self, signum, frame):
        """Handle system signals"""
        print(f"\nReceived signal {signum}")
        self.stop()


def main():
    """Main entry point"""
    try:
        app = SmartClipboardAppWithButton()
        app.start()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

