import inspect
from dataclasses import dataclass
import requests
from abc import ABC, abstractmethod


class InstanceAttrNamesGetterMixin:
    def get_attr_names(self):
        names = [name for name in vars(self)
                 if not inspect.ismethod(name)]
        return names

class DBRow(ABC):
    @abstractmethod
    def get_values_row(self):
        raise NotImplementedError()


@dataclass
class Weather(DBRow, InstanceAttrNamesGetterMixin):
    name: str
    weather_description: str
    main_temp: str
    main_pressure: str
    main_humidity: str
    wind_speed: str

    @staticmethod
    def from_json(json):
        return Weather(
            name=json["name"],
            weather_description=json["weather"][0]["description"],
            main_temp=float(json["main"]["temp"]),
            main_pressure=int(json["main"]["pressure"]),
            main_humidity=int(json["main"]["humidity"]),
            wind_speed=float(json["wind"]["speed"])
        )

    def get_values_row(self):
        return (
        self.name, self.weather_description, self.main_temp, self.main_pressure, self.main_humidity, self.wind_speed)


class OpenWeatherApiClient:
    def __init__(self, api_key: str, base_url=''):
        self.api_key = api_key
        self.base_url = base_url

    def get_weather(self, city) -> Weather:
        params = {"q": city, "appid": self.api_key, 'units': 'metric'}
        json_dict = requests.get(self.base_url, params=params).json()
        return Weather.from_json(json_dict)


if __name__ == '__main__':
    api_key = input('>')
    cities = ["New York", "London", "Warsaw"]
    apiClient = OpenWeatherApiClient(api_key)
    for city in cities:
        print(apiClient.get_weather(city).get_attr_names())

