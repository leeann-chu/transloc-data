import requests
import csv
from API_KEYS import API_KEY

thingYouWant = "stops"

url = f"https://transloc-api-1-2.p.rapidapi.com/{thingYouWant}.json"

querystring = {"agencies":"283","callback":"call"}

headers = {
	"X-RapidAPI-Key": f"{API_KEY}",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# save_file = open(f"{thingYouWant}.json", "w")  
# json.dump(response.json(), save_file, indent = 6)  
# save_file.close()  

# Opening JSON file and loading the data
# into the variable data
# with open(f'{thingYouWant}.json') as json_file:
#     data = json.load(json_file)
 
# now we will open a file for writing
data_file = open('data_file.csv', 'w', newline='')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0

for key in response.json()['data']:
    if count == 0:
        header = key.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(key.values())
 
data_file.close()