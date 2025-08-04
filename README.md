# 🌤️ Weather Dashboard

A simple, clean weather application built with Python and Tkinter that combines real-time weather data with personal features like journaling and daily inspirational quotes.

## ✨ Features

- **Real-time Weather Lookup** - Get current weather for any city worldwide
- **Weather Icons** - Visual weather icons for different conditions
- **Smart Weather Alerts** - Automatic alerts for extreme temperatures, storms, and severe weather
- **Weather History** - Track and view your recent weather searches
- **Personal Weather Journal** - Record your thoughts and experiences about the weather
- **Daily Inspirational Quotes** - Curated quotes from team members to brighten your day
- **Clean, Modern UI** - Simple interface with soft colors and rounded design elements

## 🚀 Setup Instructions

### Prerequisites
- Python 3.7 or higher
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/SamPomeroy/WeatherDashboard
   cd WeatherDashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Mac/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Create a `.env` file in the project root
   - Add your OpenWeatherMap API key:
   ```
   API_KEY=your_openweathermap_api_key_here
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage Guide

### Getting Weather Information
1. Enter a city name in the search field
2. Click "Search" or press Enter
3. View current weather, temperature, and conditions
4. Weather data is automatically saved to your history

### Using Weather Alerts
1. Enter a city name
2. Click "Alerts" to check for weather warnings
3. Get notifications for storms, extreme temperatures, and other severe conditions

### Weather Journaling
1. Enter a city to get current weather
2. Click "Journal" to open the journal entry window
3. Write your thoughts about the weather or day
4. Click "Save Entry" to store your journal entry
5. Use "View Journal" to read previous entries

### Viewing History
- Click "History" to see your last 5 weather searches
- Includes date, time, city, temperature, and conditions

### Daily Inspiration
- App shows a random inspirational quote on startup
- Click "New Quote" anytime for fresh inspiration
- Quotes are curated from team member collections

## 📁 Project Structure

```
WeatherDashboard/
├── main.py                 # Application entry point
├── config.py              # Configuration and API key setup
├── requirements.txt       # Python dependencies
├── .env                   # API key (create this file)
├── core/
│   └── api.py            # Weather API integration
├── gui/
│   └── interface.py      # Main GUI application
├── data/
│   ├── quotes.csv        # Inspirational quotes database
│   ├── weather_history.txt    # Saved weather searches
│   └── weather_journal.txt    # Personal journal entries
└── images/               # Weather icons
    ├── sun.png
    ├── cloud.png
    ├── rain.png
    └── ...
```

## 🔧 Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **API**: OpenWeatherMap API
- **Data Storage**: Text files and CSV
- **Design**: Clean, modern interface with soft colors and intuitive layout

## 🎨 Custom Features

This weather app goes beyond basic weather lookup with several personal touches:

- **Team Quotes Integration** - Displays inspirational quotes collected from team members
- **Weather Journaling** - Personal reflection and mood tracking related to weather
- **Smart Alerts** - Context-aware weather warnings and suggestions
- **Visual Design** - Custom color scheme and rounded UI elements for a modern feel
- **History Tracking** - Persistent storage of weather searches for easy reference

## 🐛 Troubleshooting

**App won't start:**
- Make sure you have Python 3.7+ installed
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify your `.env` file contains a valid API key

**No weather data:**
- Check your internet connection
- Verify your OpenWeatherMap API key is valid and active
- Make sure the city name is spelled correctly

**Icons not showing:**
- Ensure the `images/` folder contains the weather icon files
- Check that image files have the correct names (sun.png, cloud.png, etc.)

## 📄 License

This project is for educational purposes. Weather data provided by OpenWeatherMap.

---

Made with ❤️ for learning GUI development and API integration.
