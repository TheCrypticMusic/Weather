import requests
import json
import config
import os


class WeatherViewer:

    def __init__(self, location):
        self.location = location.title()
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={config.api_key}&units=metric"
        self.__test_connection()

    def __test_connection(self):
        self.res = requests.get(self.url)
        if self.res.status_code == 200:
            print('Connection made')
        else:
            print('Please try again')

    def display_weather(self):
        data = json.loads(self.res.text)
        print(data)
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        os.system(f"""
                osascript -e 'display notification "Temperature: {temp:.0f}°C\nWeather: {weather}" with title "Current Weather in {self.location}"'
                """
                  )


test = WeatherViewer(location='poole')
test.display_weather()