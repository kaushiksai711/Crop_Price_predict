import requests
import pandas as pd
from datetime import datetime, timedelta

# Define your OpenWeatherMap API key
api_key = 'a3199dd21ba69ce647ed2ccad3c13b54'

# Define the location for Warangal
latitude = 17.9784
longitude = 79.5941

# Define the time period
start_date = datetime(2011, 1, 1)
end_date = datetime.now()
date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Prepare to store the weather data
weather_data = []

# Retrieve weather data for each date
for date in date_list:
    unix_timestamp = int(date.timestamp())
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={unix_timestamp}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if 'current' in data:
        weather_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'temperature': data['current']['temp'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_speed'],
            'weather': data['current']['weather'][0]['description']
        })
    else:
        print('the')

# Create a DataFrame and save to a CSV file
df = pd.DataFrame(weather_data)
df.to_csv('warangal_weather_data_2011_2024.csv', index=False)

print(f"Saved data to warangal_weather_data_2011_2024.csv")
