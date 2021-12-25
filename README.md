# Python-Weather-app

This is a simple program I created that shows the user the current weather status in a city they search.
The data is gathered by calling an API from https://openweathermap.org/api
The GUI is created by using tkinter within python.

Simply run the program, enter a city and click enter. 

The orginal program also included a photo icon symbol to show the weather status, removed for this version for simplicity as those files would have to be downloaded

I later added in a feature that uses http://ipinfo.io/ API to automatically gather the users initial location. The initial location is used from start of program, showing the user the weather status in their city without having to search. 

Only minor issue is that cities are automatically assumed to be the most popular, for instance a search of "London" would not show the results for London Ohio.

Plan to fix this issue by using a more area specific API, could also add in user inputs for state/zipcode
