# import required modules
import argparse
import requests, json

from pythonosc import udp_client


def send_to_patch(value, str, port):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=port)
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    client.send_message(value, str)

 
# Enter your API key here
api_key = "76d2b434eef9b8323fa6931abe0599c1"
 
# base_url variable to store url
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# Cupertino latitude and longitude
latitude = 37.323
longitude = -122.032

# complete url address
complete_url = base_url + "lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=" + api_key
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object 
# convert json format data into
# python format data
x = response.json()
print(x)
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]

    current_weather = "Temperature: " +\
                    str(round(current_temperature - 273.15)) + "°C\n" + \
          "humidity: " +\
                    str(current_humidity) + "%\n" + \
          str(weather_description)

    weather_icon = z[0]["icon"]
    icon_url = "https://openweathermap.org/img/wn/" + weather_icon + ".png"

    send_to_patch("text", current_weather, 5005)
    send_to_patch("icon", icon_url, 5006)
 
else:
    print(" City Not Found ")