import os
import sys
import requests
from requests.auth import HTTPBasicAuth

import json

from exception import CustomException


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import logging 
from exception import CustomException

def load_config():
    current_dir = os.path.dirname(__file__)  # Get the directory of the script
    config_path = os.path.join(current_dir, '..', 'config.json')  # Move one directory up and locate config.json

    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
    
    
