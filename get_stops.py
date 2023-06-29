import requests
import csv
from API_KEYS import API_KEY

url = f"https://transloc-api-1-2.p.rapidapi.com/stops.json"

querystring = {"agencies":"283","callback":"call"}

headers = {
	"X-RapidAPI-Key": f"{API_KEY}",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# now we will open a file for writing
data_file = open('data_stops.csv', 'w', newline='')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing headers to the CSV file
count = 0

for key in response.json()['data']:
    if count == 0:
        header = key.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(key.values())
 
data_file.close()