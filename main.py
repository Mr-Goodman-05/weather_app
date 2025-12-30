import requests

def get_weather(city):
    """
    Fetches weather data for a given city

    Args:
        city (str): Name of city

    Returns:
        dict: Weather data from API
    """
    api_key = "763fc0c1d3ce8da9a80c4dfa4e8015f8"  # You need to get this from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    return response.json()

def main():
    """Main function to run the weather app."""
    print("=== Weather App ===")
    city = input("Enter city name: ")

    print(f"\nFetching weather for {city}...")
    weather_data = get_weather(city)

    #print the raw data (we'll improve this later)
    print(weather_data)

if __name__ == "__main__":
    main()