import pandas as pd
import requests
import time

api_url = "url"
while True:
    response = requests.get(api_url)
    w_d = response.json()
    dict = {temp: w_d[temp],humidity: w_d[humidity]}
    data= pd.DataFrame(dict)
    new_data=data
    weather_info=weather_info.append(new_data)
    weather_info=weather_info.to_csv("weather_info.csv", index=False)
    time.sleep(3600)
    

