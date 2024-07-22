import json
import requests

# define the data structure for the stuff we need
class LocationData:
    def __init__(self, name, forecastUrl, forecastHourlyUrl):
        self.name = name
        self.forecastUrl = forecastUrl
        self.forecastHourlyUrl = forecastHourlyUrl

    def get_forecast(self):
        print('todo')
        # if self.forecast is undefined, fetch it
        # return self.forecast

    def get_forecastHourly(self):
        print('todo')
        # if self.forecastHourly is undefined, fetch it
        # return self.forecastHourly


# read in file for points
f = open('input.json')
input = json.load(f)

metadata = {}
base_url = 'https://api.weather.gov/points/'
for location in input['locations']:
    name = location['name']
    lat = location['lat']
    long = location['long']

    url = base_url + str(lat) + ',' + str(long)

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            forecastUrl = response.json()['properties']['forecast']
            forecastHourlyUrl = response.json()['properties']['forecastHourly']
            metadata[name] = LocationData(name, forecastUrl, forecastHourlyUrl)
        else:
            print('issue getting metadata for point: ' + name)
            print('Error:', response.status_code)
    except Exception as e:
        print('exception when getting metdata, e is:')
        print(e)

print('metadata is:')
print(metadata)

for k, v in metadata:
    v.get_forecast()
    v.get_forecastHourly()

# for now, just print to a file

