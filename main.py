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
    print("=" * 40)
    print("         WEATHER APP")
    print("=" * 40)
    
    city = input("\nEnter city name: ")
    
    print(f"\nFetching weather for {city}...\n")
    
    try:
        weather_data = get_weather(city)
        
        # Extract useful information
        if 'main' in weather_data:
            temp_kelvin = weather_data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp_celsius:.1f}°C")
            print(f"Conditions: {description.capitalize()}")
        else:
            print("Could not retrieve weather data.")
            print("Check your API key or city name.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()