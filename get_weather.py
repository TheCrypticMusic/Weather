import requests
import json
import config


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
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        current_weather = (f"""Current weather in {self.location}
                        \nTemperature: {temp:.0f}°C\nWeather: {weather}
                        """)
        print(current_weather)


if __name__ == '__main__':
    while True:
        user_location = input("Please enter a location:\n")
        user_result = WeatherViewer(user_location)
        user_result.display_weather()
