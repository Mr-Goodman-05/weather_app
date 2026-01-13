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
    
    print(f"\nFetching weather for {city}...\n")
    
    try:
        weather_data = get_weather(city)
        
        # Extract useful information
        if 'main' in weather_data:
            temp_kelvin = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            
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
        else:
            print("Could not retrieve weather data.")
            print("Check your API key or city name.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()