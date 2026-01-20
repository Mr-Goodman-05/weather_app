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

def get_forecast(city):
    """
    Fetches 5-day weather forecast for a given city.
    
    Args:
        city (str): Name of the city
    
    Returns:
        dict: Forecast data from API
    """
    api_key = "763fc0c1d3ce8da9a80c4dfa4e8015f8"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    
    response = requests.get(url)
    return response.json()

def display_forecast(forecast_data, unit_choice):
    """
    Display 5-day forecast in a readable format.
    
    Args:
        forecast_data (dict): Forecast data from API
        unit_choice (str): Temperature unit preference (1, 2, or 3)
    """
    if 'list' not in forecast_data:
        print("Could not retrieve forecast data.")
        return
    
    print("\n" + "=" * 60)
    print("              5-DAY WEATHER FORECAST")
    print("=" * 60)
    
    # The API returns data every 3 hours, we'll show one per day (noon time)
    # We'll take every 8th entry (24 hours / 3 hours = 8 entries per day)
    daily_forecasts = forecast_data['list'][::8]
    
    for forecast in daily_forecasts[:5]:  # Limit to 5 days
        # Extract data
        date = forecast['dt_txt'].split(' ')[0]  # Get just the date part
        temp_kelvin = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        humidity = forecast['main']['humidity']
        
        # Convert temperature based on user choice
        if unit_choice == '1':
            temp = kelvin_to_celsius(temp_kelvin)
            temp_str = f"{temp:.1f}°C"
        elif unit_choice == '2':
            temp = kelvin_to_fahrenheit(temp_kelvin)
            temp_str = f"{temp:.1f}°F"
        elif unit_choice == '3':
            temp_c = kelvin_to_celsius(temp_kelvin)
            temp_f = kelvin_to_fahrenheit(temp_kelvin)
            temp_str = f"{temp_c:.1f}°C / {temp_f:.1f}°F"
        else:
            temp = kelvin_to_celsius(temp_kelvin)
            temp_str = f"{temp:.1f}°C"
        
        # Display forecast
        print(f"\nDate: {date}")
        print(f"  Temperature: {temp_str}")
        print(f"  Conditions: {description.capitalize()}")
        print(f"  Humidity: {humidity}%")
    
    print("=" * 60)

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    celsius = kelvin_to_celsius(kelvin)
    return (celsius * 9/5) + 32

def main():
    """Main function to run the weather app."""
    print("=" * 40)
    print("         WEATHER APP")
    print("=" * 40)
    
    city = input("\nEnter city name: ")
    
    # Ask user for temperature unit preference
    print("\nChoose temperature unit:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Both")
    
    unit_choice = input("Enter choice (1/2/3): ")
    
    # Ask user what they want to see
    print("\nWhat would you like to see?")
    print("1. Current weather only")
    print("2. 5-day forecast only")
    print("3. Both current weather and forecast")
    
    view_choice = input("Enter choice (1/2/3): ")
    
    print(f"\nFetching weather data for {city}...\n")
    
    try:
        # Show current weather
        if view_choice in ['1', '3']:
            print("=" * 40)
            print("        CURRENT WEATHER")
            print("=" * 40)
            
            weather_data = get_weather(city)
            
            if 'main' in weather_data:
                temp_kelvin = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                
                # Display temperature based on user choice
                if unit_choice == '1':
                    temp_celsius = kelvin_to_celsius(temp_kelvin)
                    print(f"Temperature: {temp_celsius:.1f}°C")
                elif unit_choice == '2':
                    temp_fahrenheit = kelvin_to_fahrenheit(temp_kelvin)
                    print(f"Temperature: {temp_fahrenheit:.1f}°F")
                elif unit_choice == '3':
                    temp_celsius = kelvin_to_celsius(temp_kelvin)
                    temp_fahrenheit = kelvin_to_fahrenheit(temp_kelvin)
                    print(f"Temperature: {temp_celsius:.1f}°C / {temp_fahrenheit:.1f}°F")
                else:
                    print("Invalid choice. Showing Celsius by default.")
                    temp_celsius = kelvin_to_celsius(temp_kelvin)
                    print(f"Temperature: {temp_celsius:.1f}°C")
                
                print(f"Conditions: {description.capitalize()}")
                print(f"Humidity: {humidity}%")
            else:
                print("Could not retrieve current weather data.")
                print("Check your API key or city name.")
        
        # Show forecast
        if view_choice in ['2', '3']:
            forecast_data = get_forecast(city)
            display_forecast(forecast_data, unit_choice)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()