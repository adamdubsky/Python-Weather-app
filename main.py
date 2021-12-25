#Adam Dubsky project, written in december 2021
#program is a weather app written in python 
#Uses a api key for weather data 
#using tkinter for the basic gui interface
#uses a api to get users initial location using geolocation api

#API key
#03552ea42ae5edc6ded3cf7d466d831b
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

key = '499e465aeb174ff88081e39ef599844b'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
current_loc_url = 'http://ipinfo.io/json'

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import json
from urllib.request import urlopen




#correctly formats data for api call and outputs in json format
def get_weather(location):
    output = requests.get(url.format(location, key))
    if output:
        format_json = output.json()
        country = format_json['sys']['country']
        city = format_json['name']
        kelvin = format_json['main']['temp']
        #feels_like_kel = format_json['main']['feels_like']
        #feels_like = (feels_like_kel - 237.15) * 1.8 + 32
        fahrenheit = (kelvin - 273.15) * 1.8 + 32
        current_weather = format_json['weather'][0]['description']
        icon_visual = format_json['weather'][0]['icon']
        final_output = (country,city,fahrenheit,current_weather)
        return final_output
    else:
        return None

def use_current():
    
    current_loc_call = requests.get(current_loc_url)
    curr_location = current_loc_call.json()['city']
    curr_loc_weather = get_weather(curr_location)
    if curr_loc_weather:
        label_location['text'] = '{}, {}'.format(curr_loc_weather[0], curr_loc_weather[1])
        label_temperature['text'] = '{:.1f}F'.format(curr_loc_weather[2])
        label_weather['text'] = '{}'.format(curr_loc_weather[3])
    else:
        messagebox.showerror('Error', 'City not found')



#function that takes the user input and feeds through and retrieves data for location
def search_API():
    city_output = prompt_text.get()
    weather = get_weather(city_output);
    if weather:
        label_location['text'] = '{}, {}'.format(weather[0], weather[1])
        label_temperature['text'] = '{:.1f}F'.format(weather[2])
        label_weather['text'] = '{}'.format(weather[3])
        #label_feelsLike['text'] = '{:.1f}F'.format(weather[4])
    else:
        messagebox.showerror('Error', 'City not found')



#GUI 
screen = Tk()
screen.geometry('800x350')
screen.title("Weather")

#Labels GUI
label_location = Label(screen, text = 'Location', font = ('bold', 20))
label_temperature = Label(screen, text = 'Temperature', font = ('bold', 20))
label_weather = Label(screen, text = 'Weather', font = ('bold', 20))
label_feelsLike = Label(screen, text = 'Weather', font = ('bold', 20))
label_location.pack()
label_temperature.pack()
label_weather.pack()
label_feelsLike.pack()

#handles everything around the user input prompt
prompt_text = StringVar()
prompt = Entry(screen,textvariable=prompt_text)
prompt.pack()
search_button = Button(screen, text='Enter', width = 15, command = search_API)
use_curr_button = Button(screen, text = 'Use current location', width = 15, command = use_current())
#use_curr_button.pack()
search_button.pack()



screen.mainloop()
