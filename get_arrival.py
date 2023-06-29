import requests
import csv
from API_KEYS import API_KEY

url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"

querystring = {"agencies":"283","callback":"call"}

headers = {
	"X-RapidAPI-Key": f"{API_KEY}",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# did not get to finish because the endpoint went silent
for key in response.json()['data']:
    print(key)