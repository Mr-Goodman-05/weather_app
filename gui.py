import tkinter as tk
from tkinter import ttk, messagebox
from main import get_weather, get_forecast, kelvin_to_celsius, kelvin_to_fahrenheit

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Weather App", 
                               font=('Arial', 24, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # City input
        ttk.Label(main_frame, text="City Name:", 
                 font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.city_entry = ttk.Entry(main_frame, width=30, font=('Arial', 12))
        self.city_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Temperature unit selection
        ttk.Label(main_frame, text="Temperature Unit:", 
                 font=('Arial', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.unit_var = tk.StringVar(value="celsius")
        unit_frame = ttk.Frame(main_frame)
        unit_frame.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(unit_frame, text="Celsius", variable=self.unit_var, 
                       value="celsius").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(unit_frame, text="Fahrenheit", variable=self.unit_var, 
                       value="fahrenheit").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(unit_frame, text="Both", variable=self.unit_var, 
                       value="both").pack(side=tk.LEFT, padx=5)
        
        # View selection
        ttk.Label(main_frame, text="View:", 
                 font=('Arial', 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
        
        self.view_var = tk.StringVar(value="current")
        view_frame = ttk.Frame(main_frame)
        view_frame.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(view_frame, text="Current", variable=self.view_var, 
                       value="current").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(view_frame, text="Forecast", variable=self.view_var, 
                       value="forecast").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(view_frame, text="Both", variable=self.view_var, 
                       value="both").pack(side=tk.LEFT, padx=5)
        
        # Get Weather button
        self.get_weather_btn = ttk.Button(main_frame, text="Get Weather", 
                                         command=self.fetch_weather)
        self.get_weather_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Results text area
        self.result_text = tk.Text(main_frame, height=25, width=60, 
                                   font=('Courier', 10), wrap=tk.WORD)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Scrollbar for results
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, 
                                 command=self.result_text.yview)
        scrollbar.grid(row=5, column=2, sticky=(tk.N, tk.S))
        self.result_text.config(yscrollcommand=scrollbar.set)
        
        # Bind Enter key to fetch weather
        self.city_entry.bind('<Return>', lambda event: self.fetch_weather())
        
    def format_temperature(self, temp_kelvin):
        """Format temperature based on user selection."""
        unit = self.unit_var.get()
        
        if unit == "celsius":
            temp = kelvin_to_celsius(temp_kelvin)
            return f"{temp:.1f}°C"
        elif unit == "fahrenheit":
            temp = kelvin_to_fahrenheit(temp_kelvin)
            return f"{temp:.1f}°F"
        else:  # both
            temp_c = kelvin_to_celsius(temp_kelvin)
            temp_f = kelvin_to_fahrenheit(temp_kelvin)
            return f"{temp_c:.1f}°C / {temp_f:.1f}°F"
    
    def display_current_weather(self, weather_data):
        """Display current weather in the text area."""
        if 'main' not in weather_data:
            self.result_text.insert(tk.END, "Could not retrieve current weather data.\n")
            self.result_text.insert(tk.END, "Check your API key or city name.\n")
            return
        
        self.result_text.insert(tk.END, "=" * 50 + "\n")
        self.result_text.insert(tk.END, "        CURRENT WEATHER\n")
        self.result_text.insert(tk.END, "=" * 50 + "\n\n")
        
        temp_kelvin = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        temp_str = self.format_temperature(temp_kelvin)
        
        self.result_text.insert(tk.END, f"Temperature: {temp_str}\n")
        self.result_text.insert(tk.END, f"Conditions: {description.capitalize()}\n")
        self.result_text.insert(tk.END, f"Humidity: {humidity}%\n\n")
    
    def display_forecast(self, forecast_data):
        """Display 5-day forecast in the text area."""
        if 'list' not in forecast_data:
            self.result_text.insert(tk.END, "Could not retrieve forecast data.\n")
            return
        
        self.result_text.insert(tk.END, "=" * 50 + "\n")
        self.result_text.insert(tk.END, "        5-DAY WEATHER FORECAST\n")
        self.result_text.insert(tk.END, "=" * 50 + "\n\n")
        
        from datetime import datetime
        
        forecasts_by_date = {}
        today = datetime.now().strftime('%Y-%m-%d')
        
        for forecast in forecast_data['list']:
            date = forecast['dt_txt'].split(' ')[0]
            
            if date == today:
                continue
            
            if date not in forecasts_by_date:
                forecasts_by_date[date] = forecast
        
        daily_forecasts = list(forecasts_by_date.values())[:5]
        
        for forecast in daily_forecasts:
            date = forecast['dt_txt'].split(' ')[0]
            temp_kelvin = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            humidity = forecast['main']['humidity']
            
            temp_str = self.format_temperature(temp_kelvin)
            
            self.result_text.insert(tk.END, f"Date: {date}\n")
            self.result_text.insert(tk.END, f"  Temperature: {temp_str}\n")
            self.result_text.insert(tk.END, f"  Conditions: {description.capitalize()}\n")
            self.result_text.insert(tk.END, f"  Humidity: {humidity}%\n\n")
    
    def fetch_weather(self):
        """Fetch and display weather based on user selections."""
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Show loading message
        self.result_text.insert(tk.END, f"Fetching weather data for {city}...\n\n")
        self.root.update()
        
        view = self.view_var.get()
        
        try:
            # Show current weather
            if view in ['current', 'both']:
                weather_data = get_weather(city)
                # Clear loading message
                self.result_text.delete(1.0, tk.END)
                self.display_current_weather(weather_data)
            
            # Show forecast
            if view in ['forecast', 'both']:
                forecast_data = get_forecast(city)
                if view == 'forecast':
                    self.result_text.delete(1.0, tk.END)
                self.display_forecast(forecast_data)
        
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"An error occurred: {e}\n")
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()