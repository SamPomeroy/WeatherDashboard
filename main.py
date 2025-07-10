# main.py
import sys
from pathlib import Path

# Add WeatherDashboard root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tkinter import Tk
from gui.interface import WeatherAppGUI

if __name__ == "__main__":
    root = Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
