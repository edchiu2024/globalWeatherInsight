import os
import json
import sys
common_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
sys.path.append(common_path)

from logger import logging 
from exception import CustomException
from datetime import datetime
from utils import load_config
import requests

class BaseExtractor:
    def __init__(self, api_url, headers=None):
        self.api_url = api_url
        self.headers = headers

    def fetch_data(self, endpoint):
import os
import json
import sys
common_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
sys.path.append(common_path)

from logger import logging 
from exception import CustomException
from datetime import datetime
from utils import load_config
import requests

class BaseExtractor:
    def __init__(self, api_url, headers=None):
        self.api_url = api_url
        self.headers = headers

    def fetch_data(self, endpoint):
       try:
            response = requests.get(f"{self.api_url}/{endpoint}", headers=self.headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
       except Exception as e:
            logging.error(f"Error fetching data from API: {e}")
            raise CustomException(e,sys) 

    def process_data(self, data):
        raise NotImplementedError("This method should be overridden by subclasses.")

class WeatherExtractor(BaseExtractor):
    def process_data(self, data):
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

class CountryExtractor(BaseExtractor):
    def process_data(self, data):
        return {
            "name": data["name"],
            "population": data["population"]
        }

    def process_data(self, data):
        raise NotImplementedError("This method should be overridden by subclasses.")

class WeatherExtractor(BaseExtractor):
    def process_data(self, data):
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

class CountryExtractor(BaseExtractor):
    def process_data(self, data):
        return {
            "name": data["name"],
            "population": data["population"]
        }