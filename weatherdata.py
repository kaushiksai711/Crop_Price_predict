from datetime import datetime, timedelta
import pandas as pd
from meteostat import Point, Daily

# Define the location (latitude, longitude, and elevation) for Warangal
warangal = Point(17.9784, 79.5941, 302)

# Define the time period
end = datetime.now()
start = end - timedelta(days=13*365)  # Past 13 years

# Retrieve daily data for the specified time period and location
data = Daily(warangal, start, end)
data = data.fetch()

# Print the retrieved data (optional)
print(data.head())

# Save the data to a CSV file
file_name = 'warangal_weather_data_past_13_years.csv'
data.to_csv(file_name)
print(f"Saved data to {file_name}")
