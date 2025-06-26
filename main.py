import tkinter as tk
from config import API_KEY
import requests

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    return response.json()

def get_weather():
    city = city_entry.get()
    data = fetch_weather(city)
    output_label.config(text=str(data))

# GUI setup
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x200")

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack()

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
