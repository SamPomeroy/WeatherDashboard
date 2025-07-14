# 🌦️ WeatherDashboard

A cute and functional desktop weather assistant built with Python and Tkinter. This project allows users to fetch weather data by city, track history, receive alerts, and journal weather observations — all with a clean, friendly GUI.

---

## 🚀 Features

- 🔍 **City-based Weather Lookup**: Enter a city and get the current weather conditions (temperature + description).
- 📜 **View History**: Stores past searches for quick recall.
- ⚠️ **Weather Alerts**: Displays warnings or alerts based on fetched data.
- 📝 **Journal Entry**: Add notes about the current weather, mood, or events.
- 🎨 **Modern UI**: Soft colors, rounded edges, emoji-enhanced buttons, and responsive layout.
- 🖼️ **Custom Icons**: Includes weather-themed images like clouds, sun, wind, and more (future integration in progress).

---

## 🧱 Folder Structure

```
WeatherDashboard/
│
├── core/
│   └── api.py                # Handles API interaction
│
├── features/
│   ├── alerts/
│   │   └── feature.py        # Weather alert logic
│   ├── history/
│   │   └── feature.py        # Saves and displays search history
│   └── journal/
│       └── feature.py        # Journal entry pop-up and saving
│
├── gui/
│   └── interface.py          # Main GUI logic and layout
│
├── images/                   # Weather icons (clouds, sun, wind, etc.)
│
├── data/                     # History/journal storage (e.g., CSV or JSON)
│
├── main.py                   # Entry point (optional wrapper for interface)
└── README.md                 # This file
```

---

## ⚙️ How to Run It

1. Make sure you have Python 3.8+ installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WeatherDashboard.git
   cd WeatherDashboard
   ```
3. Install dependencies (if any; currently Tkinter is included by default).
4. Run the GUI:
   ```bash
   python gui/interface.py
   ```

---

## 💻 Interface Preview

Here's a snapshot of the current version of the Weather Dashboard GUI:

![Weather Dashboard Screenshot](images/screenshot.png)

---

## 🛣️ Future Enhancements

- Tabbed layout (like a dashboard UI)
- Icon integration with weather types
- Save journal entries to disk with timestamp
- Toggle dark/light mode
- Weekly forecast display

---

## 🙋 About Me

Built by Samantha Shuler-Pomeroy as part of the Justice Through Code capstone project. I’m exploring how to make tech approachable, kind, and useful — even when it’s cloudy ☁️💻

---

## 📜 License

MIT — do what you want, just don’t blame me if it rains 😄

Week 13 API Check-in

After accidentally breaking some things during my skills check (oops), I got it working again! I added buttons for viewing history, alerts, and adding journal entries in the upcoming features. Forecast and chart panels are still in progress. Next step: refine the layout and finish data visualization features.