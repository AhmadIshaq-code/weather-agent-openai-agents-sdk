import os
import requests

from dotenv import load_dotenv
from agents import function_tool

load_dotenv()


@function_tool
def get_weather(city: str) -> str:

    api_key = os.getenv("WEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return str(data)