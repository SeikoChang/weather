#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
#from weather import Forecast
import urllib.parse
import json
#from datetime import datetime
import datetime

url = 'http://api.openweathermap.org/data/2.5/weather'
access_token = '7b6f99b4800bac916762cc5a85031bda'


class Forecast(object):
    def __init__(self, city='Taipei'):
        self.city = city
        self.data = get_forecast_json(city)
        #print(json.dumps(self.data, indent=4, sort_keys=True)) 

    def __str__(self):
        return 'City = [{0}]'.format(self.getCity())

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getData(self):
        return self.data

    def setData(self):
        self.data  = get_forecast_json(self.city)
        print(json.dumps(self.data, indent=4, sort_keys=True)) 

    def temperatue_avg(self):
        weather = self.getData()
        temperatue = 0
        if weather:
            temperatue = weather['main']['temp'] - 273.15 #temp_in_celsius

        return temperatue

    def temperatue_min(self):
        weather = self.getData()
        temperatue = 0
        if weather:
            temperatue = weather['main']['temp_min'] - 273.15 #temp_in_celsius

        return temperatue

    def temperatue_max(self):
        weather = self.getData()
        temperatue = 0
        if weather:
            temperatue = weather['main']['temp_max'] - 273.15 #temp_in_celsius

        return temperatue

    def timestamp(self):
        weather = self.getData()
        timestamp = 0
        if weather:
            timestamp = datetime.datetime.utcnow()

        return timestamp

    def humidity(self):
        weather = self.getData()
        humidity = 0
        if weather:
            humidity = weather['main']['humidity']

        return humidity

    def pressure(self):
        weather = self.getData()
        pressure = 0
        if weather:
            pressure = weather['main']['pressure']

        return pressure

    def cityname(self):
        weather = self.getData()
        cityname = 0
        if weather:
            cityname = weather['name']

        return cityname

    def description(self):
        weather = self.getData()
        description = 0
        if weather:
            description = weather['weather'][0]['description']

        return description

    def wind(self):
        weather = self.getData()
        deg = speed = 0
        if weather:
            deg = weather['wind']['deg']
            speed = weather['wind']['speed']

        return deg, speed

    def clouds(self):
        weather = self.getData()
        clouds = 0
        if weather:
            clouds = weather['clouds']['all']

        return clouds

    def sunrise(self):
        weather = self.getData()
        sunrise = 0
        if weather:
            sunrise = weather['sys']['sunrise']

        return sunrise

    def sunset(self):
        weather = self.getData()
        sunset = 0
        if weather:
            sunset = weather['sys']['sunset']

        return sunset

    def timezone(self):
        weather = self.getData()
        timezone = 0
        if weather:
            timezone = weather['timezone']

        return timezone

    def overall(self):
        cityname = self.cityname()
        timezone = self.timezone()
        timezone = '{:02d}:{:02d}'.format(*divmod(timezone, 3600))
        temperatue_avg = round(float(self.temperatue_avg()), 2)
        temperatue_min = round(float(self.temperatue_min()), 2)
        temperatue_max = round(float(self.temperatue_max()), 2)
        timestamp = str(self.timestamp())+' + '+timezone
        pressure = self.pressure()
        humidity = self.humidity()
        description = self.description()
        wind_deg, wind_speed  = self.wind()
        clouds = self.clouds()
        sunrise = self.sunrise()
        sunrise = datetime.datetime.utcfromtimestamp(int(sunrise)).strftime('%Y-%m-%d %H:%M:%S')+' + '+timezone
        sunset = self.sunset()
        sunset = datetime.datetime.utcfromtimestamp(int(sunset)).strftime('%Y-%m-%d %H:%M:%S')+' + '+timezone


        out = '\
城市: {city}\n\
時區: {timezone}\n\
雲量: {description}\n\
平均溫度: {temperatue_avg}\n\
最低溫度: {temperatue_min}\n\
最高溫度: {temperatue_max}\n\
氣壓: {pressure} hpa\n\
風速: {wind_speed} m/s\n\
風向: {wind_deg}\n\
濕度: {humidity} %\n\
當地日出時間: {sunrise}\n\
當地日落時間: {sunset}\n\
當地目前時間: {timestamp}\n\
               '.format(description=description, temperatue_avg=temperatue_avg, temperatue_min=temperatue_min, temperatue_max=temperatue_max, timestamp=timestamp, pressure=pressure, city=cityname, humidity=humidity, wind_speed=wind_speed, wind_deg=wind_deg, sunrise=sunrise, sunset=sunset, timezone=timezone)

        #print(out)
        return out

def get_forecast_json(city='Taipei'):
    encoded_city_name = urllib.parse.quote(city)
    #country_code = 'us'

    #r = requests.get('{url}?q={encoded_city_name},{country_code}&APPID={access_token}'.format(
    r = requests.get('{url}?q={encoded_city_name}&APPID={access_token}'.format(
        url = url, 
        encoded_city_name = encoded_city_name, 
        #country_code = country_code, 
        access_token = access_token))

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None


if __name__ == "__main__":
    city = 'Taipei'
    print(Forecast(city=city).overall())
    pass

