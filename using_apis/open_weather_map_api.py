import xmltodict
import os
import requests

api_key = os.environ["OWM_API_KEY"]
city_name = "Bishkek"

url = (f"https://api.openweathermap.org/data/2.5/weather?"
       f"q={city_name}&appid={api_key}&units=metric&mode=xml")

xml_str = requests.get(url).text
weather_dict = xmltodict.parse(xml_str)

print(weather_dict["current"]["temperature"])
print(weather_dict["current"]["humidity"])
