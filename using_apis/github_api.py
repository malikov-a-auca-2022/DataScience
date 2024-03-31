import os
import requests

username = "malikov-a-auca-2022"
token = os.environ['GITHUB_TOKEN']

url = f"https://api.github.com/user/repos"

response = requests.get(url, headers={
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
})

repos = response.json()
print("{: <50} Private".format("Name"))
for repo in repos:
    print("{: <50} {: <5}"
          .format(repo['name'], str(repo['private'])))
