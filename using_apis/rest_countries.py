import json
import requests

country_name = "suomi"
url = f"https://restcountries.com/v3.1/name/{country_name}"

json_str = requests.get(url).text
country_dict = json.loads(json_str)

pretty = json.dumps(country_dict, indent=2)
print(pretty)