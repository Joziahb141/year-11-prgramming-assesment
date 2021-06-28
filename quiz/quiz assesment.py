import requests

response = requests.get("http://api.open-notify.org/astros.json")

for astronaut in response.json()['people']:
    print('name', astronaut['name'])