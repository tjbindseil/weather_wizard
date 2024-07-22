import json
import requests

def make_request(url):
    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            print('issue getting metadata for point: ' + name)
            print('Error:', response.status_code)
            raise Exception()
    except Exception as e:
        print('exception when getting metdata, e is:')
        print(e)

# define the data structure for the stuff we need
class LocationData:
    def __init__(self, name, lat, long, forecastUrl, forecastHourlyUrl):
        self.name = name
        self.lat = lat
        self.long = long
        self.forecastUrl = forecastUrl
        self.forecastHourlyUrl = forecastHourlyUrl
        self.forecast = False
        self.forecastHourly = False

    def get_forecast(self):
        if not self.forecast:
            cleaned_forecast = {}
            full_forecast = make_request(self.forecastUrl)

            cleaned_forecast['elevation'] = full_forecast['properties']['elevation']
            cleaned_forecast['periods'] = []
            for period in full_forecast['properties']['periods']:
                cleaned_period = {}
                cleaned_period['name'] = period['name']
                cleaned_period['temperature'] = period['temperature']
                cleaned_period['temperatureUnit'] = period['temperatureUnit']
                cleaned_period['probabilityOfPrecipitation'] = period['probabilityOfPrecipitation']
                cleaned_period['windSpeed'] = period['windSpeed']
                cleaned_period['windDirection'] = period['windDirection']
                cleaned_period['shortForecast'] = period['shortForecast']
                cleaned_period['detailedForecast'] = period['detailedForecast']

                cleaned_forecast['periods'].append(cleaned_period)
            self.forecast = cleaned_forecast
        return self.forecast

    def get_forecastHourly(self):
        # TODO how to get lightning data? had trouble finding in docs:
        # * https://www.weather.gov/documentation/services-web-api#/default/gridpoint_forecast_hourly
        if not self.forecastHourly:
            self.forecastHourly = make_request(self.forecastHourlyUrl)
        return self.forecastHourly


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
    response_json = make_request(url)

    forecastUrl = response_json['properties']['forecast']
    forecastHourlyUrl = response_json['properties']['forecastHourly']
    metadata[name] = LocationData(name, lat, long, forecastUrl, forecastHourlyUrl)

output = {}
for k, v in metadata.items():
    output[k] = {}
    output[k]['lat'] = v.lat
    output[k]['long'] = v.long
    output[k]['forecast'] = v.get_forecast()
    output[k]['forecastHourly'] = v.get_forecastHourly()

# for now, just print to a file
with open('output.json', 'w') as fp:
    json.dump(output, fp, indent=2)
