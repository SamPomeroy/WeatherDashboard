#!/usr/bin/env python3
"""
Weather Dashboard - Main Entry Point
A simple, cute weather app with quotes, history, alerts, and journaling
"""

import sys
from pathlib import Path
from tkinter import Tk, messagebox

# Add project root to path for imports
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

try:
    from gui.interface import WeatherAppGUI
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you're running from the project root directory")
    sys.exit(1)


def main():
    """Main entry point for the Weather Dashboard"""
    try:
        root = Tk()
        
        # Set window icon if available
        try:
            icon_path = project_root / "images" / "sun.png"
            if icon_path.exists():
                root.iconphoto(True, root.tk.call('image', 'create', 'photo', '-file', str(icon_path)))
        except Exception:
            pass  # Icon not critical
        
        # Create and run app
        app = WeatherAppGUI(root)
        
        # Center window on screen
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Fatal Error", f"Application failed to start: {str(e)}")
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
