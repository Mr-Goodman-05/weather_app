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

Fetching weather for London...
{'weather': [{'main': 'Clouds', 'description': 'overcast clouds'}], 'main': {'temp': 280.32}}
```

## Future Improvements

- [x] Better formatted output
- [x] Temperature unit conversion (Celsius/Fahrenheit)
- [ ] 5-day forecast
- [x] Error handling for invalid cities

## License

MIT License