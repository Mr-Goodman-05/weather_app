# Weather App

A simple command-line weather application built with Python.

## Description

This app fetches current weather data for any city using the OpenWeatherMap API.

## Prerequisites

- Python 3.11 or higher
- OpenWeatherMap API key (get one free at https://openweathermap.org/api)

## Installation

1. Clone this repository:
```bash
git clone git@github.com:Mr-Goodman-05/weather-app.git
cd weather-app
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your API key:
   - Open `main.py`
   - Replace `"your_api_key_here"` with your actual API key

## Usage

Run the application:
```bash
python main.py
```

Enter a city name when prompted.

## Example
```
=== Weather App ===
Enter city name: London

Choose temperature unit:
1. Celsius (°C)
2. Fahrenheit (°F)
3. Both
Enter choice (1/2/3): 1

What would you like to see?
1. Current weather only
2. 5-day forecast only
3. Both current weather and forecast
Enter choice (1/2/3): 3

Fetching weather data for London...

========================================
        CURRENT WEATHER
========================================
Temperature: 7.2°C
Conditions: Overcast clouds
Humidity: 81%

============================================================
              5-DAY WEATHER FORECAST
============================================================

Date: 2026-01-21
  Temperature: 8.5°C
  Conditions: Light rain
  Humidity: 85%

Date: 2026-01-22
  Temperature: 6.3°C
  Conditions: Scattered clouds
  Humidity: 78%

...
```

## Future Improvements

- [x] Better formatted output
- [x] Temperature unit conversion (Celsius/Fahrenheit)
- [x] 5-day forecast
- [x] Error handling for invalid cities

## License

MIT License