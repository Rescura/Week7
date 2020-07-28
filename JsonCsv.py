import requests
import pprint
import json
import csv

url = "https://api.covid19api.com/dayone/country/south-korea/status/confirmed"
response = requests.get(url)
dictData = json.loads(response.content)

with open('covid19.csv', mode='w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=',')
    for country in dictData:
        writer.writerow([country["Date"], country["Cases"]])