from time import strftime, time, sleep
from tkinter import *
from datetime import *
from dotenv import load_dotenv
import os
import requests, json 
import calendar 
from PIL import ImageTk, Image
import pendulum
import sched, time
from threading import Thread

load_dotenv()
#Getting API key from ENV file
api_key = os.getenv('API')
#Creating weekday abbreviations
weekDays = ("Monday ","Tuesday","Wednesday ","Thursday","Friday ","Saturday","Sunday")

def get_current():
    #Getting current weather from API

    url_current = 'http://dataservice.accuweather.com/currentconditions/v1/47173?apikey=' + api_key
    response_current = requests.get(url_current) 
    #checking HTTP response, filling in with dummy data if it's not 200
    if (response_current.status_code == 200):
        current_json = response_current.json()
    else:
        current_json = [
                {
                    "LocalObservationDateTime": "2021-02-24T16:18:00-08:00",
                    "EpochTime": 1614212280,
                    "WeatherText": "Cloudy",
                    "WeatherIcon": 1,
                    "HasPrecipitation": False,
                    "PrecipitationType": True,
                    "IsDayTime": True,
                    "Temperature": {
                    "Metric": {
                        "Value": 0.0,
                        "Unit": "C",
                        "UnitType": 17
                    },
                    "Imperial": {
                        "Value": 43,
                        "Unit": "F",
                        "UnitType": 18
                    }
                    },
                    "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/current-weather/47173?lang=en-us",
                    "Link": "http://www.accuweather.com/en/ca/richmond/v6y/current-weather/47173?lang=en-us"
                }
            ]
    return current_json

def get_forecast():
    #Getting weather forecast from API

    url_forecast = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/47173?apikey=' + api_key + '&metric=true'
    response_forecast = requests.get(url_forecast)

    #checking HTTP response, filling in with dummy data if it's not 200
    if (response_forecast.status_code == 200):        
        forecast_json = response_forecast.json()
    else:
        forecast_json = {
            "Headline": {
                "EffectiveDate": "2021-02-24T19:00:00-08:00",
                "EffectiveEpochDate": 1614222000,
                "Severity": 5,
                "Text": "Rain tonight",
                "Category": "rain",
                "EndDate": "2021-02-25T07:00:00-08:00",
                "EndEpochDate": 1614265200,
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/extended-weather-forecast/47173?unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?unit=c&lang=en-us"
            },
            "DailyForecasts": [
                {
                "Date": "2021-02-24T07:00:00-08:00",
                "EpochDate": 1614178800,
                "Temperature": {
                    "Minimum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    },
                    "Maximum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    }
                },
                "Day": {
                    "Icon": 1,
                    "IconPhrase": "Mostly cloudy",
                    "HasPrecipitation": False
                },
                "Night": {
                    "Icon": 1,
                    "IconPhrase": "Rain",
                    "HasPrecipitation": True,
                    "PrecipitationType": "Rain",
                    "PrecipitationIntensity": "Light"
                },
                "Sources": [
                    "AccuWeather"
                ],
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=1&unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=1&unit=c&lang=en-us"
                },
                {
                "Date": "2021-02-25T07:00:00-08:00",
                "EpochDate": 1614265200,
                "Temperature": {
                    "Minimum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    },
                    "Maximum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    }
                },
                "Day": {
                    "Icon": 1,
                    "IconPhrase": "Intermittent clouds",
                    "HasPrecipitation": False
                },
                "Night": {
                    "Icon": 1,
                    "IconPhrase": "Partly cloudy",
                    "HasPrecipitation": False
                },
                "Sources": [
                    "AccuWeather"
                ],
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=2&unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=2&unit=c&lang=en-us"
                },
                {
                "Date": "2021-02-26T07:00:00-08:00",
                "EpochDate": 1614351600,
                "Temperature": {
                    "Minimum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    },
                    "Maximum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    }
                },
                "Day": {
                    "Icon": 1,
                    "IconPhrase": "Mostly sunny",
                    "HasPrecipitation": False
                },
                "Night": {
                    "Icon": 1,
                    "IconPhrase": "Mostly clear",
                    "HasPrecipitation": False
                },
                "Sources": [
                    "AccuWeather"
                ],
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=3&unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=3&unit=c&lang=en-us"
                },
                {
                "Date": "2021-02-27T07:00:00-08:00",
                "EpochDate": 1614438000,
                "Temperature": {
                    "Minimum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    },
                    "Maximum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    }
                },
                "Day": {
                    "Icon": 1,
                    "IconPhrase": "Mostly cloudy",
                    "HasPrecipitation": False
                },
                "Night": {
                    "Icon": 1,
                    "IconPhrase": "Showers",
                    "HasPrecipitation": True,
                    "PrecipitationType": "Rain",
                    "PrecipitationIntensity": "Light"
                },
                "Sources": [
                    "AccuWeather"
                ],
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=4&unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=4&unit=c&lang=en-us"
                },
                {
                "Date": "2021-02-28T07:00:00-08:00",
                "EpochDate": 1614524400,
                "Temperature": {
                    "Minimum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    },
                    "Maximum": {
                    "Value": 00.0,
                    "Unit": "C",
                    "UnitType": 17
                    }
                },
                "Day": {
                    "Icon": 1,
                    "IconPhrase": "Rain",
                    "HasPrecipitation": True,
                    "PrecipitationType": "Rain",
                    "PrecipitationIntensity": "Light"
                },
                "Night": {
                    "Icon": 1,
                    "IconPhrase": "Rain",
                    "HasPrecipitation": True,
                    "PrecipitationType": "Rain",
                    "PrecipitationIntensity": "Light"
                },
                "Sources": [
                    "AccuWeather"
                ],
                "MobileLink": "http://m.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=5&unit=c&lang=en-us",
                "Link": "http://www.accuweather.com/en/ca/richmond/v6y/daily-weather-forecast/47173?day=5&unit=c&lang=en-us"
                }
            ]
            }
    return forecast_json

def update_time_date():
    #Updating time/date/day labels in an infinite while loop

    #infinite while loop running every 0.1 seconds to update the clock/date/day
    while True:
        
        #Getting today's date
        today_date = date.today()

        #update time
        current_time = strftime('%I:%M:%S')
        lbl_time.configure(text = current_time)
        lbl_AMPM.configure(text= strftime('%p'))
        #update date
        current_date = today_date.strftime("%d %b %Y")
        lbl_date.configure(text = current_date)
        #update day
        current_day = today_date.strftime("%A")
        lbl_day.configure(text = current_day)

        time.sleep(0.1)

def update_api():
    #Updatest the API for current weather, forecast, and sunrise/sunset

    #Creating empty dictionaries for icons and forecast
    icons = {}
    forecast = {}

    #Populating dictionary for icon files
    for i in range(1,45):
        if i not in [9, 10, 27, 28]:
            icons[str(i)] = ImageTk.PhotoImage(Image.open('icons/' + str(i) + '.png'))

    #Infinite while loop that runs once per hour to update the API data
    while True:

        print('update API = ' + strftime('%I:%M:%S %p') + '--------')

        #Getting JSON data from accuweather API
        forecast_json = get_forecast()
        current_json = get_current()

        #Getting
        response_sunrise_sunset = requests.get('https://api.sunrise-sunset.org/json?lat=49.166592&lng=-123.133568&formatted=0')
        sunrise_sunset_json = response_sunrise_sunset.json()    

        #Getting sunrise time from API and formatting it into string
        sunrise = sunrise_sunset_json['results']['sunrise']
        sunrise_utc = pendulum.parse(sunrise, tz='UTC')
        sunrise_pst = sunrise_utc.in_timezone("US/Pacific")
        sunrise_pst_str = sunrise_pst.format('h:mm A')

        #Getting sunset time from API and foramtting it into string
        sunset = sunrise_sunset_json['results']['sunset']
        sunset_utc = pendulum.parse(sunset, tz='UTC')
        sunset_pst = sunset_utc.in_timezone("US/Pacific")
        sunset_pst_str = sunset_pst.format('h:mm A')

        print('Sunrise/Sunset: ' + sunrise_pst_str + ' ' + sunset_pst_str)

        #creating forecast within forecast dictionary for the 5 day forecast
        for i in range(0,5):
            forecast['day_of_week' + str(i)] = weekDays[(date.today()+ timedelta(i)).weekday()]
            forecast['temp_low' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Minimum']['Value'])
            forecast['temp_high' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Maximum']['Value'])
            forecast['icon_day' + str(i)] = str(forecast_json['DailyForecasts'][i]['Day']['Icon'])
            forecast['icon_night' + str(i)] = str(forecast_json['DailyForecasts'][i]['Night']['Icon'])

        current_temperature = current_json[0]['Temperature']['Metric']['Value']
        print('New Current Tepurature: ' + str(current_temperature))

        current_weather_icon_num = str(current_json[0]['WeatherIcon'])
        current_weather_icon = ImageTk.PhotoImage(Image.open('icons/' + current_weather_icon_num + '.png'))
        print('Current weather icon! : ' + str(current_weather_icon_num))

        for i in range(0,5):
            forecast['day_of_week' + str(i)] = weekDays[(date.today()+ timedelta(i)).weekday()]
            forecast['temp_low' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Minimum']['Value'])
            forecast['temp_high' + str(i)] = str(forecast_json['DailyForecasts'][i]['Temperature']['Maximum']['Value'])
            forecast['icon_day' + str(i)] = str(forecast_json['DailyForecasts'][i]['Day']['Icon'])
            forecast['icon_night' + str(i)] = str(forecast_json['DailyForecasts'][i]['Night']['Icon'])

        for x in forecast:
            print('Day ' + str(x) + ' ' + forecast['temp_high0'] + ' ' + forecast['temp_low0'])

        #update current wather
        lbl_weather_current.configure(text = str(current_temperature))
        lbl_weather_current_img.configure(image = current_weather_icon)

        # lbl_high0.configure(text= forecast['temp_high0'] + ' Low: ' + forecast['temp_low0'], bg="blue", fg="white", font = ("Times", 10, 'bold'))
        lbl_day0.configure(text= forecast['day_of_week0'])
        lbl_high0.configure(text= forecast['temp_high0'])
        lbl_low0.configure(text= forecast['temp_low0'])
        lbl_weather_day_0_img.configure(image = icons[forecast['icon_day0']])
        lbl_weather_night_0_img.configure(image =  icons[forecast['icon_night0']])

        lbl_day1.configure(text= forecast['day_of_week1'])   
        lbl_high1.configure(text= forecast['temp_high1'])
        lbl_low1.configure(text= forecast['temp_low1'])
        lbl_weather_day_1_img.configure(image = icons[forecast['icon_day1']])
        lbl_weather_night_1_img.configure(image =  icons[forecast['icon_night1']])

        lbl_day2.configure(text= forecast['day_of_week2'])
        lbl_high2.configure(text= forecast['temp_high2'])
        lbl_low2.configure(text= forecast['temp_low2'])
        lbl_weather_day_2_img.configure(image = icons[forecast['icon_day2']])
        lbl_weather_night_2_img.configure(image =  icons[forecast['icon_night2']])

        lbl_day3.configure(text= forecast['day_of_week3'])
        lbl_high3.configure(text= forecast['temp_high3'])
        lbl_low3.configure(text= forecast['temp_low3'])
        lbl_weather_day_3_img.configure(image = icons[forecast['icon_day3']])
        lbl_weather_night_3_img.configure(image =  icons[forecast['icon_night3']])

        lbl_day4.configure(text= forecast['day_of_week4'])
        lbl_high4.configure(text= forecast['temp_high4'])
        lbl_low4.configure(text= forecast['temp_low4'])
        lbl_weather_day_4_img.configure(image = icons[forecast['icon_day4']])
        lbl_weather_night_4_img.configure(image =  icons[forecast['icon_night4']])



        #update sunrise/sunset 
        lbl_sunrise.configure(text= sunrise_pst_str)
        lbl_sunset.configure(text= sunset_pst_str)

        #sleep for an hour
        time.sleep(3600) 

#Begin create GUI
root = Tk()
root.geometry("670x480")

root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=0)
root.configure(bg='#23272A')

#Time/Date/Day Frame
frm_datetime = Frame(root)
frm_datetime.grid(row=0, column=0, sticky='w')
frm_datetime.configure(bg='#23272A')

frm_time = Frame(frm_datetime)
frm_time.grid(row=0, column=0)
frm_time.configure(bg='#23272A')

lbl_time = Label(frm_time, fg="white", font = ("Arial", 50, 'bold'), relief='flat')
lbl_time.grid(row=0, column=0, sticky='w', padx= (20,0))
lbl_time.configure(bg='#23272A')

lbl_AMPM = Label(frm_time, fg="white", font = ("Arial", 15, 'bold'), relief='flat')
lbl_AMPM.grid(row=0, column=1, sticky='s', padx= (0,20))
lbl_AMPM.configure(bg='#23272A')


lbl_date = Label(frm_datetime, fg="white", font = ("Arial", 30, 'bold'), relief='flat')
lbl_date.grid(column = 0, row= 1)
lbl_date.configure(bg='#23272A')

lbl_day = Label(frm_datetime, fg="white", font = ("Arial", 30, 'bold'), relief='flat')
lbl_day.grid(column = 0, row= 2)
lbl_day.configure(bg='#23272A')


#Sunrise/Sunset frame

frm_sunrise_sunset = Frame(frm_datetime)
frm_sunrise_sunset.grid(row=3, column=0)
frm_sunrise_sunset.configure(bg='#23272A')

lbl_sunrise = Label(frm_sunrise_sunset, fg="orange", font = ("Times", 15, 'bold'))
lbl_sunrise.grid(row=0 ,column=0, padx= (30,30), pady= (10,10))
lbl_sunrise.configure(bg='#23272A')

lbl_sunset = Label(frm_sunrise_sunset, fg="#c111d9", font = ("Times", 15, 'bold'))
lbl_sunset.grid(row=0 ,column=1, padx= (30,30), pady= (10,10))
lbl_sunset.configure(bg='#23272A')

#Weather Frame

#Current Weather

frm_weather = Frame(root)
frm_weather.grid(row=0, column=2, sticky=NW)
frm_weather.configure(bg='#23272A')


lbl_weather_current = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 25, 'bold'),  borderwidth= 5, relief="groove")
lbl_weather_current.grid(row=0,column=0, sticky=NW)

lbl_weather_current_img = Label(frm_weather)
lbl_weather_current_img.grid(row=0,column=1, sticky=NW)
lbl_weather_current_img.configure(bg='#23272A')

#Weather Forecast

lbl_day0 = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_day0.grid(row=1,column=0, sticky=NW)
lbl_high0 = Label(frm_weather, bg="#FF4500", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_high0.grid(row=2,column=0, sticky=NW)
lbl_low0 = Label(frm_weather, bg="blue", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_low0.grid(row=2,column=1, sticky=NW)
lbl_weather_day_0_img = Label(frm_weather)
lbl_weather_day_0_img.grid(row=2,column=2, sticky=NW)
lbl_weather_day_0_img.configure(bg='#23272A')
lbl_weather_night_0_img = Label(frm_weather)
lbl_weather_night_0_img.grid(row=2,column=3, sticky=NW)
lbl_weather_night_0_img.configure(bg='#23272A')

lbl_day1 = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_day1.grid(row=3,column=0, sticky=NW)
lbl_high1 = Label(frm_weather, bg="#FF4500", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_high1.grid(row=4,column=0, sticky=NW)
lbl_low1 = Label(frm_weather, bg="blue", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_low1.grid(row=4,column=1, sticky=NW)
lbl_weather_day_1_img = Label(frm_weather)
lbl_weather_day_1_img.grid(row=4,column=2, sticky=NW)
lbl_weather_day_1_img.configure(bg='#23272A')
lbl_weather_night_1_img = Label(frm_weather)
lbl_weather_night_1_img.grid(row=4,column=3, sticky=NW)
lbl_weather_night_1_img.configure(bg='#23272A')

lbl_day2 = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_day2.grid(row=5,column=0, sticky=NW)
lbl_high2 = Label(frm_weather, bg="#FF4500", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_high2.grid(row=6,column=0, sticky=NW)
lbl_low2 = Label(frm_weather, bg="blue", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_low2.grid(row=6,column=1, sticky=NW)
lbl_weather_day_2_img = Label(frm_weather)
lbl_weather_day_2_img.grid(row=6,column=2, sticky=NW)
lbl_weather_day_2_img.configure(bg='#23272A')
lbl_weather_night_2_img = Label(frm_weather)
lbl_weather_night_2_img.grid(row=6,column=3, sticky=NW)
lbl_weather_night_2_img.configure(bg='#23272A')

lbl_day3 = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_day3.grid(row=7,column=0, sticky=NW)
lbl_high3 = Label(frm_weather, bg="#FF4500", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_high3.grid(row=8,column=0, sticky=NW)
lbl_low3 = Label(frm_weather, bg="blue", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_low3.grid(row=8,column=1, sticky=NW)
lbl_weather_day_3_img = Label(frm_weather)
lbl_weather_day_3_img.grid(row=8,column=2, sticky=NW)
lbl_weather_day_3_img.configure(bg='#23272A')
lbl_weather_night_3_img = Label(frm_weather)
lbl_weather_night_3_img.grid(row=8,column=3, sticky=NW)
lbl_weather_night_3_img.configure(bg='#23272A')

lbl_day4 = Label(frm_weather, bg="#23272A", fg="white", font = ("Times", 10, 'bold'), relief='flat')
lbl_day4.grid(row=9,column=0, sticky=NW)
lbl_high4 = Label(frm_weather, bg="#FF4500", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_high4.grid(row=10,column=0, sticky=NW)
lbl_low4 = Label(frm_weather, bg="blue", fg="white", font = ("Times", 15, 'bold'), relief='flat')
lbl_low4.grid(row=10,column=1, sticky=NW)
lbl_weather_day_4_img = Label(frm_weather)
lbl_weather_day_4_img.grid(row=10,column=2, sticky=NW)
lbl_weather_day_4_img.configure(bg='#23272A')
lbl_weather_night_4_img = Label(frm_weather)
lbl_weather_night_4_img.grid(row=10,column=3, sticky=NW)
lbl_weather_night_4_img.configure(bg='#23272A')


#Screnblank frame

frm_screenblank = Frame(root)
frm_screenblank.grid(row=2, column=0, sticky='w')
frm_screenblank.configure(bg='#23272A')

#Button to turn screenblank to 1 h 30 m

btn_screen_on = Button(frm_screenblank, text="Screen On", command=lambda: os.system("xset dpms 7800 7800 7800"), bg="#99AAB5")
btn_screen_on.grid(row=0, column=0, padx = (80,20))

#Button to turn screenblank to 30 seconds

btn_screen_off = Button(frm_screenblank, text="Screen Off", command=lambda: os.system("xset dpms 30 30 30"), bg="#99AAB5")
btn_screen_off.grid(row=0, column=1, padx = (35,20))

#running thread to update time/date/day of GUI
update_time_date_thread = Thread(target= update_time_date, daemon = True)
update_time_date_thread.start()

#running thread to update API data (current weather, forecast, sunrise/sunset)
update_api_thread = Thread(target= update_api, daemon = True)
update_api_thread.start()

root.mainloop()
