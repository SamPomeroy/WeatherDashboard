# features/alerts/feature.py

class AlertsFeature:
    def check_alerts(self, data: dict) -> str:
        if "weather" not in data:
            return "⚠️ Unable to check alerts."

        desc = data["weather"][0]["description"].lower()
        temp = data.get("main", {}).get("temp", 0)
        wind = data.get("wind", {}).get("speed", 0)

        alerts = []

        # Weather description-based alerts
        if "storm" in desc or "thunder" in desc:
            alerts.append("⛈️ Severe Thunderstorm Alert!")
        elif "rain" in desc:
            alerts.append("🌧️ Rainy – Grab an Umbrella.")
        elif "snow" in desc:
            alerts.append("❄️ Snow – Drive Carefully.")
        elif "fog" in desc or "mist" in desc or "haze" in desc:
            alerts.append("🌫️ Low Visibility Warning.")
        elif "clear" in desc:
            alerts.append("☀️ Clear Skies – Great Day Ahead!")

        # Temperature-based alerts
        if temp > 95:
            alerts.append("🔥 Heat Warning – Stay Hydrated!")
        elif temp < 32:
            alerts.append("🥶 Freezing Temps – Bundle Up!")

        # Wind-based alerts
        if wind > 20:
            alerts.append(f"💨 Wind Advisory – {wind} mph gusts!")

        return "\n".join(alerts) if alerts else "✅ No active weather alerts."
