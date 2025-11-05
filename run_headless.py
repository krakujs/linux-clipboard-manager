#!/usr/bin/env python3
"""
Smart Clipboard Manager - Headless Mode
Runs the clipboard manager without GUI for demonstration
"""
import sys
import time
import signal
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import Config
from src.storage import ClipboardStorage
from src.content_analyzer import ContentAnalyzer
from src.clipboard_monitor import ClipboardMonitor


class HeadlessClipboardApp:
    """Headless version of clipboard manager for demonstration"""
    
    def __init__(self):
        """Initialize the application"""
        print("\n" + "="*60)
        print("SMART CLIPBOARD MANAGER - HEADLESS MODE")
        print("="*60)
        print("\nStarting Smart Clipboard Manager in headless mode...")
        print("(This version runs without GUI for demonstration)\n")
        
        # Initialize components
        self.config = Config()
        print(f"✅ Config loaded from: {self.config.config_path}")
        
        db_path = self.config.get_database_path()
        self.storage = ClipboardStorage(str(db_path))
        print(f"✅ Database: {db_path}")
        
        self.analyzer = ContentAnalyzer()
        print(f"✅ Content analyzer initialized")
        
        # Track statistics
        self.clips_captured = 0
        self.running = True
        
        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        print(f"✅ Smart Clipboard Manager is ready!")
        print("\n" + "-"*60)
    
    def _on_clipboard_change(self, content):
        """Handle clipboard change"""
        self.clips_captured += 1
        
        print(f"\n[{self.clips_captured}] 📋 Clipboard changed!")
        print(f"    Content: {content[:60]}...")
        
        # Analyze
        analysis = self.analyzer.analyze(content)
        print(f"    Type: {analysis['content_type']}")
        
        if analysis['is_sensitive']:
            print(f"    🔒 SENSITIVE - Not saving")
            return
        
        # Save
        clip_id = self.storage.save_clip(
            content=content,
            content_type=analysis['content_type'],
            metadata=analysis['metadata']
        )
        
        if clip_id:
            print(f"    ✅ Saved as ID: {clip_id}")
        else:
            print(f"    ℹ️  Duplicate - updated timestamp")
        
        # Show stats every 5 clips
        if self.clips_captured % 5 == 0:
            self._show_stats()
    
    def _show_stats(self):
        """Show current statistics"""
        stats = self.storage.get_stats()
        print(f"\n    📊 Stats: {stats['total']} total clips, {stats['favorites']} favorites")
    
    def start_monitoring(self):
        """Start clipboard monitoring"""
        print("\n🔍 Starting clipboard monitoring...")
        print("   Monitoring interval: 0.5 seconds")
        print("   Press Ctrl+C to stop\n")
        
        monitor = ClipboardMonitor(
            callback=self._on_clipboard_change,
            interval=0.5
        )
        
        monitor.start()
        
        # Simulate some clipboard activity for demonstration
        print("="*60)
        print("DEMONSTRATION MODE")
        print("="*60)
        print("\nSimulating clipboard activity...\n")
        
        demo_clips = [
            "https://github.com/user/awesome-project",
            "contact@example.com",
            "def calculate_sum(a, b):\n    return a + b",
            '{"name": "Smart Clipboard", "version": "1.0.0"}',
            "Remember to buy: milk, eggs, bread, coffee",
            "https://stackoverflow.com/questions/12345",
            "admin@company.com",
            "SELECT * FROM users WHERE active = 1;",
            "TODO: Finish the clipboard manager project",
            "pip install smart-clipboard-manager",
        ]
        
        for i, clip in enumerate(demo_clips, 1):
            time.sleep(1)
            self._on_clipboard_change(clip)
            
            if i == 5:
                print("\n" + "-"*60)
                print("Halfway through demonstration...")
                print("-"*60)
        
        print("\n" + "="*60)
        print("DEMONSTRATION COMPLETE")
        print("="*60)
        
        # Show final statistics
        self._show_final_stats()
        
        # Show recent history
        self._show_recent_history()
        
        # Demonstrate search
        self._demonstrate_search()
        
        # Keep running
        print("\n" + "="*60)
        print("APPLICATION RUNNING")
        print("="*60)
        print("\nThe clipboard manager is now running in the background.")
        print("In a real environment with GUI:")
        print("  - Press Ctrl+Shift+V to open the clipboard manager")
        print("  - Search, filter, and paste from history")
        print("  - Mark favorites, view statistics")
        print("\nPress Ctrl+C to stop the application...")
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        
        monitor.stop()
    
    def _show_final_stats(self):
        """Show final statistics"""
        print("\n📊 FINAL STATISTICS")
        print("-"*60)
        
        stats = self.storage.get_stats()
        print(f"Total clips captured: {self.clips_captured}")
        print(f"Total clips in database: {stats['total']}")
        print(f"Favorites: {stats['favorites']}")
        print(f"\nBy type:")
        for content_type, count in sorted(stats['by_type'].items()):
            icon = self._get_type_icon(content_type)
            print(f"  {icon} {content_type:15} : {count}")
    
    def _show_recent_history(self):
        """Show recent clipboard history"""
        print("\n📋 RECENT CLIPBOARD HISTORY")
        print("-"*60)
        
        history = self.storage.get_history(limit=5)
        for i, clip in enumerate(history, 1):
            icon = self._get_type_icon(clip['content_type'])
            preview = clip['content'][:50].replace('\n', ' ')
            print(f"{i}. {icon} [{clip['content_type']:8}] {preview}...")
    
    def _demonstrate_search(self):
        """Demonstrate search functionality"""
        print("\n🔍 SEARCH DEMONSTRATION")
        print("-"*60)
        
        search_terms = ['github', 'example', 'def']
        
        for term in search_terms:
            results = self.storage.search(term)
            print(f"\nSearch for '{term}': {len(results)} result(s)")
            for result in results[:2]:  # Show max 2 results
                preview = result['content'][:40].replace('\n', ' ')
                print(f"  - {preview}...")
    
    def _get_type_icon(self, content_type):
        """Get icon for content type"""
        icons = {
            'url': '🔗',
            'email': '📧',
            'code': '💻',
            'json': '{}',
            'text': '📄',
            'file_path': '📁',
            'number': '🔢',
            'markdown': '📝',
        }
        return icons.get(content_type, '📄')
    
    def _signal_handler(self, signum, frame):
        """Handle system signals"""
        print(f"\n\n⚠️  Received signal {signum}")
        self.stop()
    
    def stop(self):
        """Stop the application"""
        print("\n" + "="*60)
        print("SHUTTING DOWN")
        print("="*60)
        
        self.running = False
        
        # Show final stats
        stats = self.storage.get_stats()
        print(f"\n✅ Captured {self.clips_captured} clipboard changes")
        print(f"✅ Stored {stats['total']} unique clips")
        
        # Close storage
        self.storage.close()
        print(f"✅ Database closed")
        
        print("\n👋 Thank you for using Smart Clipboard Manager!")
        print("="*60 + "\n")
        
        sys.exit(0)


def main():
    """Main entry point"""
    try:
        app = HeadlessClipboardApp()
        app.start_monitoring()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

