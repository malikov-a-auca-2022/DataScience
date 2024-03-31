import requests

url = "https://cataas.com/cat/ginger"
output_file = "cat.jpg"
response = requests.get(url)

with open(output_file, 'wb') as f:
    f.write(response.content)
    print("Cat image was saved!")
