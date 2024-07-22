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

#### JSON
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

This can be hard to read, so there will also be an html output.

#### html
In addition, the forecast (not hourly forecast (yet...)) will be shown in a table.

##### no lightening
https://forecast.weather.gov/MapClick.php?lat=37.6603&lon=-119.1739&unit=0&lg=english&FcstType=graphical

##### with lightening
https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w10u=0&w11=lal&w12u=1&AheadHour=0&Submit=Submit&FcstType=graphical&textField1=37.6603&textField2=-119.1739&site=all&unit=0&dd=&bw=
