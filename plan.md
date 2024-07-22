# Climb-It app
An app that will greatly simplify your search for the perfect weather window!

## Usage

### Input
Supply a json file in the following format:

```
{
  "locations"': [
    {
      "name": "clyde minaret",
      "lat": 37.6618,
      "long": -119.1781
    },
    {
      "name": "mt whitney",
      "lat": 36.5785,
      "long": -118.2919
    }
  ]
}
```

#### Notes
* latitude and longitude must be truncated to 4 decimal points

### Output

The weather at each point will be printed in a similar format as the input. For example:

```
{
  "locations"': [
    {
      "name": "clyde minaret",
      "lat": 37.6618,
      "long": -119.1781,
      "forecast": {
         ...
      },
      "forecastHourly": {
         ...
      }
    },
    {
      "name": "mt whitney",
      "lat": 36.5785,
      "long": -118.2919,
      "forecast": {
         ...
      },
      "forecastHourly": {
         ...
      }
    }
  ]
}
```
