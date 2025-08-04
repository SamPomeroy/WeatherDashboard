import tkinter as tk
from tkinter import Toplevel, Text
import os
import csv
import random
from pathlib import Path
from datetime import datetime
from core.api import fetch_weather


class WeatherAppGUI:
    def __init__(self, root):
        """
        Main application class for the Weather Dashboard.
        Sets up UI, loads icons & quotes, and displays a random quote on start.
        """
        self.root = root
        self.root.title("Weather Dashboard")
        self.root.geometry("400x550")
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(False, False)

        # Project root path
        self.project_root = Path(__file__).resolve().parent.parent

        # Load assets
        self.weather_icons = self.load_icons()
        self.quotes = self.load_quotes()

        # Build the interface
        self.setup_ui()

        # Show a random quote at startup
        self.show_random_quote()

    # ---------------- ICON LOADING ----------------
    def load_icons(self):
        """Load small weather icons from /images folder."""
        from tkinter import PhotoImage
        icons = {}
        icon_dir = self.project_root / "images"

        icon_files = {
            "clear": "sun.png",
            "clouds": "cloud.png",
            "rain": "rain.png",
            "snow": "snow.png",
            "thunderstorm": "storm.png",
            "default": "thermometer.png"
        }

        for key, filename in icon_files.items():
            path = icon_dir / filename
            if path.exists():
                try:
                    icons[key] = PhotoImage(file=str(path))
                except:
                    pass
        return icons

    # ---------------- QUOTES LOADING ----------------
    def load_quotes(self):
        """Load quotes from data/quotes.csv with fallback defaults."""
        quotes = []
        quotes_file = self.project_root / "data" / "quotes.csv"

        try:
            if quotes_file.exists():
                with open(quotes_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        quote = row.get("Quote", "").strip().strip('"')
                        author = row.get("Author", "").strip()
                        if quote and author:
                            quotes.append(f'"{quote}"\n— {author}')
        except:
            pass

        if not quotes:
            quotes = [
                '"Every day is a fresh start."\n— Unknown',
                '"The weather is perfect for staying positive."\n— Me'
            ]
        return quotes

    # ---------------- CUSTOM POPUP ----------------
    def show_custom_message(self, title, message, bg_color="#f8f9fa", accent="#e3f2fd"):
        """
        Custom popup styled to match the app with pastel accent color.
        """
        popup = Toplevel(self.root)
        popup.title(title)
        popup.configure(bg=bg_color)
        popup.resizable(False, False)
        popup.grab_set()
        popup.transient(self.root)

        # Size the popup
        popup_width = 360
        popup_height = 220
        popup.geometry(f"{popup_width}x{popup_height}")

        # Center popup on the main window (not the entire screen)
        self.root.update_idletasks()  # Make sure main window geometry is updated
        
        # Get main window position and size
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_width = self.root.winfo_width()
        main_height = self.root.winfo_height()
        
        # Calculate center position relative to main window
        x = main_x + (main_width // 2) - (popup_width // 2)
        y = main_y + (main_height // 2) - (popup_height // 2)
        
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Container
        container = tk.Frame(popup, bg=bg_color, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # Title
        tk.Label(
            container, text=title,
            font=("Helvetica", 14, "bold"),
            bg=bg_color, fg="#495057"
        ).pack(pady=(0, 10))

        # Message box (rounded illusion)
        msg_frame = tk.Frame(container, bg="white", relief="flat", bd=0)
        msg_frame.pack(fill="both", expand=True, pady=(0, 15))

        msg_text = Text(
            msg_frame, font=("Helvetica", 10),
            bg="white", fg="#495057",
            relief="flat", wrap="word", height=6
        )
        msg_text.pack(fill="both", expand=True, padx=10, pady=10)
        msg_text.insert("1.0", message)
        msg_text.config(state="disabled")

        # OK button
        btn_frame = tk.Frame(container, bg=accent)
        btn_frame.pack(pady=(5, 0))

        tk.Button(
            btn_frame, text="OK",
            font=("Helvetica", 10),
            bg=accent, fg="#1976d2",
            activebackground="#bbdefb",
            relief="flat", bd=0,
            cursor="hand2",
            command=popup.destroy
        ).pack(padx=15, pady=5)

    # ---------------- RANDOM QUOTE ----------------
    def show_random_quote(self):
        """Select and display a random quote in the output box."""
        if self.quotes:
            quote = random.choice(self.quotes)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"Daily Inspiration\n\n{quote}")

    # ---------------- MAIN UI ----------------
    def setup_ui(self):
        """Build the main weather dashboard layout."""
        container = tk.Frame(self.root, bg="#f8f9fa", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # Title
        tk.Label(container, text="Weather Dashboard",
                 font=("Helvetica", 18, "bold"),
                 bg="#f8f9fa", fg="#495057").pack(pady=(0, 15))

        # Search area
        entry_frame = tk.Frame(container, bg="white", relief="flat", bd=0)
        entry_frame.pack(fill="x", pady=(0, 10))

        self.city_entry = tk.Entry(
            entry_frame, font=("Helvetica", 12),
            relief="flat", bg="white", fg="#495057"
        )
        self.city_entry.pack(fill="x", padx=10, pady=8)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())

        # Search button
        tk.Button(container, text="Search",
                  font=("Helvetica", 10),
                  bg="#e3f2fd", fg="#1976d2",
                  activebackground="#bbdefb",
                  relief="flat", bd=0,
                  cursor="hand2",
                  command=self.get_weather).pack(pady=(0, 15))

        # Weather icon
        self.icon_label = tk.Label(container, bg="#f8f9fa")
        self.icon_label.pack(pady=5)

        # Output box (rounded illusion)
        text_frame = tk.Frame(container, bg="white", relief="flat", bd=0)
        text_frame.pack(fill="both", expand=True, pady=(0, 10))

        self.output_text = tk.Text(
            text_frame, font=("Helvetica", 11),
            bg="white", fg="#495057",
            relief="flat", wrap="word", height=10
        )
        self.output_text.pack(fill="both", expand=True, padx=15, pady=15)

        # Action buttons
        tk.Button(container, text="History",
                  font=("Helvetica", 9),
                  bg="#f3e5f5", fg="#7b1fa2",
                  activebackground="#e1bee7",
                  relief="flat", bd=0,
                  command=self.show_history).pack(fill="x", pady=(2, 2))

        tk.Button(container, text="Alerts",
                  font=("Helvetica", 9),
                  bg="#ffebee", fg="#c62828",
                  activebackground="#ffcdd2",
                  relief="flat", bd=0,
                  command=self.show_alerts).pack(fill="x", pady=(2, 2))

        tk.Button(container, text="Journal",
                  font=("Helvetica", 9),
                  bg="#e8f5e8", fg="#2e7d32",
                  activebackground="#c8e6c9",
                  relief="flat", bd=0,
                  command=self.add_journal_entry).pack(fill="x", pady=(2, 2))

        tk.Button(container, text="New Quote",
                  font=("Helvetica", 9),
                  bg="#fff3e0", fg="#f57c00",
                  activebackground="#ffe0b2",
                  relief="flat", bd=0,
                  command=self.show_random_quote).pack(fill="x", pady=(2, 2))

        # View Journal button
        tk.Button(container, text="View Journal",
                  font=("Helvetica", 9),
                  bg="#e8f5e8", fg="#2e7d32",
                  activebackground="#c8e6c9",
                  relief="flat", bd=0,
                  cursor="hand2",
                  command=self.show_journal_entries).pack(fill="x", pady=(2, 0))

    # ---------------- WEATHER FETCH ----------------
    def get_weather(self):
        """Fetch and display weather for entered city."""
        city = self.city_entry.get().strip()
        if not city:
            self.show_custom_message("Missing City", "Please enter a city first!", accent="#ffebee")
            return

        data = fetch_weather(city)
        if "error" in data:
            self.show_custom_message("Error", data["error"], accent="#ffebee")
            return

        # Extract weather info
        desc = data["weather"][0]["description"]
        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]

        # Set weather icon
        weather_main = data["weather"][0]["main"].lower()
        icon = self.weather_icons.get(weather_main, self.weather_icons.get("default"))
        if icon:
            self.icon_label.config(image=icon)
            self.icon_label.image = icon

        # Display in output box
        info = (
            f"{city.title()}\n{desc.title()}\n"
            f"{temp}°F (feels like {feels_like}°F)\n"
            f"Humidity: {humidity}%"
        )
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, info)

        self.save_to_history(city, temp, desc)

    # ---------------- HISTORY ----------------
    def save_to_history(self, city, temp, desc):
        """Append weather info to history file."""
        history_file = self.project_root / "data" / "weather_history.txt"
        with open(history_file, "a") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
            f.write(f"{timestamp}, {city}, {temp}°F, {desc}\n")

    def show_history(self):
        """Show last 5 history entries."""
        history_file = self.project_root / "data" / "weather_history.txt"
        if not history_file.exists():
            self.show_custom_message("History", "No history yet!", accent="#e3f2fd")
            return

        with open(history_file, "r") as f:
            lines = f.readlines()
        recent = lines[-5:]
        self.show_custom_message("Weather History", "".join(recent), accent="#e3f2fd")

    # ---------------- ALERTS ----------------
    def show_alerts(self):
        """Show weather alerts based on simple rules."""
        city = self.city_entry.get().strip()
        if not city:
            self.show_custom_message("Alerts", "Enter a city first!", accent="#ffebee")
            return

        data = fetch_weather(city)
        if "error" in data:
            self.show_custom_message("Error", data["error"], accent="#ffebee")
            return

        desc = data["weather"][0]["description"].lower()
        temp = data.get("main", {}).get("temp", 0)

        alerts = []
        if "storm" in desc or "thunder" in desc:
            alerts.append("Storm warning!")
        elif "rain" in desc:
            alerts.append("Bring umbrella!")
        if temp > 90:
            alerts.append("Very hot!")
        elif temp < 32:
            alerts.append("Freezing!")

        alert_text = "\n".join(alerts) if alerts else "No alerts"
        self.show_custom_message("Weather Alerts", alert_text, accent="#ffebee")

    # ---------------- JOURNAL ----------------
    def add_journal_entry(self):
        """Open a popup to add a journal entry."""
        city = self.city_entry.get().strip()
        if not city:
            self.show_custom_message("Journal", "Enter a city first!", accent="#e8f5e8")
            return

        journal_file = self.project_root / "data" / "weather_journal.txt"

        def save_entry_and_close():
            content = entry.get("1.0", tk.END).strip()
            if not content:
                self.show_custom_message("Empty Entry", "Please write something before saving!", accent="#ffebee")
                return
            with open(journal_file, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
                f.write(f"{timestamp}, {city}: {content}\n")
            self.show_custom_message("Saved", "Journal entry saved!", accent="#e8f5e8")
            popup.destroy()

        # Popup window
        popup = Toplevel(self.root)
        popup.title("Weather Journal")
        popup.configure(bg="#f8f9fa")
        popup.resizable(False, False)
        popup.grab_set()
        popup.transient(self.root)
        
        # Size and center on main window
        popup_width = 340
        popup_height = 260
        popup.geometry(f"{popup_width}x{popup_height}")
        
        # Center on main window
        self.root.update_idletasks()
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_width = self.root.winfo_width()
        main_height = self.root.winfo_height()
        
        x = main_x + (main_width // 2) - (popup_width // 2)
        y = main_y + (main_height // 2) - (popup_height // 2)
        
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Title
        tk.Label(
            popup, text=f"Journal for {city}",
            font=("Helvetica", 12, "bold"),
            bg="#f8f9fa", fg="#495057"
        ).pack(pady=10)

        # Text frame
        text_frame = tk.Frame(popup, bg="white", relief="flat", bd=0)
        text_frame.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        entry = Text(
            text_frame, font=("Helvetica", 10),
            bg="white", fg="#495057",
            relief="flat", wrap="word", height=6
        )
        entry.pack(fill="both", expand=True, padx=8, pady=8)
        entry.focus()

        # Save button with pastel green frame
        save_btn_frame = tk.Frame(popup, bg="#e8f5e8", relief="flat", bd=0)
        save_btn_frame.pack(pady=10)

        tk.Button(
            save_btn_frame, text="Save Entry",
            font=("Helvetica", 10, "bold"),
            bg="#e8f5e8", fg="#2e7d32",
            activebackground="#c8e6c9",
            relief="flat", bd=0,
            cursor="hand2",
            command=save_entry_and_close
        ).pack(padx=15, pady=5)

    def show_journal_entries(self):
        """Show recent journal entries in a styled popup."""
        journal_file = self.project_root / "data" / "weather_journal.txt"

        if not journal_file.exists():
            self.show_custom_message("Journal", "No journal entries yet!", accent="#e8f5e8")
            return

        try:
            with open(journal_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            recent_entries = "".join(lines[-5:]) if lines else "No entries found."

            # Styled popup
            self.show_custom_message(
                "Journal Entries",
                recent_entries,
                accent="#e8f5e8"
            )

        except Exception as e:
            self.show_custom_message("Error", f"Could not read journal: {e}", accent="#ffebee")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
