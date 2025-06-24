#  Weather App with Raspberry Pi Pico W

A weather-monitoring IoT project using the **Raspberry Pi Pico W** microcontroller.  
It connects to a Wi-Fi network, fetches real-time weather data, and displays it on a screen or serial output.

## Features
- Wi-Fi connectivity using Pico W
- Fetch real-time weather data from API (e.g. OpenWeatherMap)
- Parse JSON data (temperature, humidity, etc.)
- Display data via:
  - OLED / LCD screen *(αν έχεις)*
  - Serial monitor / REPL
- Lightweight Python (MicroPython or CircuitPython)

## Technologies & Hardware
- 🖥️ **Raspberry Pi Pico W**
- 🧠 **MicroPython**
- 🌐 `urequests` or `ureq` (for HTTP requests)
- 📡 Wi-Fi (via onboard chip)
- *(προαιρετικά)* OLED display (I2C), DHT11 sensor, etc.

## Getting Started

### 1. Flash MicroPython
- Use [Thonny IDE](https://thonny.org/) or `esptool.py` to flash MicroPython firmware on your Pico W.

### 2. Install Required Files
Upload the following Python files to the Pico:
- `main.py` – main app loop
- `wifi.py` – connects to Wi-Fi
- `weather.py` – handles API request
- `secrets.py` – (create this) with your Wi-Fi + API key:

```python
# secrets.py
WIFI_SSID = "your_wifi"
WIFI_PASSWORD = "your_password"
API_KEY = "your_openweathermap_key"
CITY = "Athens"
