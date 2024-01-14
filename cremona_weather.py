import os
import requests
import threading, time
from string import Template
from dotenv import load_dotenv

load_dotenv()
TOMORROW_KEY = os.environ.get("TOMORROW_KEY")
TIMESTEP = os.environ.get("TIMESTEP")
UNITS= os.environ.get("UNITS")

def get_weather_data(lat,lon,apiKey,timestep,units):
    URL = Template('https://api.tomorrow.io/v4/weather/forecast?location=$lat,$lon&apikey=$apiKey&fields=temperature&timesteps=$timestep&units=$units')
    r = requests.get(url = URL.substitute(lat=lat,lon=lon,apiKey=apiKey,timestep=timestep,units=units))
    data = r.json()
    # return data['data']['timelines'][0]['intervals'][0]
    # return data.timelines.minutely[0].values.temperature
    # return data['timelines']['hourly'][0]['values']['temperature']
    return data['timelines']['daily'][0]['values']['temperatureAvg']


if __name__ == "__main__":
    weather = get_weather_data(45.6427,25.5887,TOMORROW_KEY,TIMESTEP, UNITS)
    print(weather)
