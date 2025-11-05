#!/usr/bin/env python3
"""
Demo script to test Smart Clipboard Manager components
"""
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import Config
from src.storage import ClipboardStorage
from src.content_analyzer import ContentAnalyzer


def demo_content_analyzer():
    """Demo content analyzer"""
    print("\n" + "="*60)
    print("CONTENT ANALYZER DEMO")
    print("="*60)
    
    analyzer = ContentAnalyzer()
    
    test_cases = [
        "https://www.github.com/user/repo",
        "contact@example.com",
        "def hello():\n    print('Hello, World!')",
        '{"name": "John", "age": 30}',
        "# Markdown Header\nThis is **bold**",
        "Just plain text",
        "password: MySecretP@ss123",
    ]
    
    for content in test_cases:
        result = analyzer.analyze(content)
        preview = analyzer.get_preview(content, 40)
        
        print(f"\nContent: {preview}")
        print(f"  Type: {result['content_type']}")
        print(f"  Sensitive: {result['is_sensitive']}")
        if result['metadata']:
            print(f"  Metadata: {result['metadata']}")


def demo_storage():
    """Demo storage system"""
    print("\n" + "="*60)
    print("STORAGE DEMO")
    print("="*60)
    
    # Use temporary database
    storage = ClipboardStorage("demo_clipboard.db")
    
    # Save some clips
    clips = [
        ("https://www.example.com", "url"),
        ("test@email.com", "email"),
        ("print('Hello')", "code"),
        ("Just some text", "text"),
    ]
    
    print("\nSaving clips...")
    for content, content_type in clips:
        clip_id = storage.save_clip(content, content_type)
        print(f"  Saved: {content[:30]}... (ID: {clip_id})")
    
    # Get history
    print("\nRetrieving history...")
    history = storage.get_history(limit=10)
    for clip in history:
        print(f"  [{clip['id']}] {clip['content_type']}: {clip['content'][:40]}...")
    
    # Search
    print("\nSearching for 'example'...")
    results = storage.search("example")
    for clip in results:
        print(f"  Found: {clip['content'][:40]}...")
    
    # Stats
    print("\nStorage statistics:")
    stats = storage.get_stats()
    print(f"  Total clips: {stats['total']}")
    print(f"  By type: {stats['by_type']}")
    
    # Cleanup
    storage.close()
    print("\nDemo database saved as: demo_clipboard.db")


def demo_config():
    """Demo configuration system"""
    print("\n" + "="*60)
    print("CONFIGURATION DEMO")
    print("="*60)
    
    config = Config()
    
    print(f"\nConfig file: {config.config_path}")
    print(f"Database path: {config.get_database_path()}")
    print(f"Max history: {config.get('max_history')}")
    print(f"Hotkey: {config.get('hotkey')}")
    print(f"Monitor interval: {config.get('monitor_interval')}s")
    print(f"Excluded apps: {config.get('excluded_apps')}")


def main():
    """Run all demos"""
    print("\n" + "="*60)
    print("SMART CLIPBOARD MANAGER - COMPONENT DEMO")
    print("="*60)
    
    try:
        demo_config()
        demo_content_analyzer()
        demo_storage()
        
        print("\n" + "="*60)
        print("✅ All demos completed successfully!")
        print("="*60)
        print("\nTo start the full application, run:")
        print("  python main.py")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

