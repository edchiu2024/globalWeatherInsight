import os
import json
import sys
common_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
sys.path.append(common_path)

from logger import logging 
from exception import CustomException
import requests


class BaseExtractor:

    def __init__(self, config, headers=None, params=None):
        self.api_url=config['api_url']
        self.api_endpoint=config['endpoint']


        self.headers={'Content-Type': 'application/json'} 
        self.params=params

    def fetch_data(self):
        
        try:
            response=requests.get(f'{self.api_url}/{self.api_endpoint}',headers=self.headers, params=self.params)
            logging.info(f"API call endpoint: {response.url}")
            response.raise_for_status()
            return response.json()
        
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise CustomException(e,sys)
        
    def save_raw_data(self,data):
        try:
            # TODO: Implement saving raw data to S3
            pass
        
        except Exception as e:
            logging.error(f"Error saving raw data to S3: {e}")
            raise CustomException(e,sys)        
        
    def process_data(self, data, city):
        raise NotImplementedError("This should be implemented by the subclass")

class WeatherExtractor(BaseExtractor):

    def __init__(self, config, headers=None, params=None):
        super().__init__(config, headers, params)
        self.params['appid']=config['api_key']
    def fetch_data(self):
        
        try:

            response=requests.get(f'{self.api_url}/{self.api_endpoint}',headers=self.headers, params=self.params)
            logging.info(f"API call endpoint: {response.url}")
            response.raise_for_status()
            return response.json()
        
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise CustomException(e,sys)


    def process_data(self, data,city):
        weather_data=[]
        for object in data['list']:
            weather_object={}

            weather_object['dt']=object['dt']
            weather_object['dt_txt']=object['dt_txt']
            weather_object['city']=city
            weather_object['temp']=object['main']['temp']
            weather_object['feels_like']=object['main']['feels_like']
            weather_object['temp_min']=object['main']['temp_min']
            weather_object['temp_max']=object['main']['temp_max']
            weather_object['pressure']=object['main']['pressure']
            weather_object['humidity']=object['main']['humidity']
            weather_object['weather']=object['weather'][0]['main']
            weather_object['cloud_level']=object['clouds']['all']
            weather_object['wind_speed']=object['wind']['speed']
            weather_object['wind_direction']=object['wind']['deg']
            weather_object['gust_direction'] = object.get('wind', {}).get('gust', None)
            weather_object['visibility'] = object.get('visibility', None)

            weather_data.append(weather_object)


        return weather_data
    
class CountryExtractor(BaseExtractor):
    def process_data(self, data,city):
        #logic 
        return data    