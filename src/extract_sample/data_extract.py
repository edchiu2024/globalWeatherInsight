# ETL job for Reddit interview
import os
import json
import sys
common_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
sys.path.append(common_path)

from logger import logging 
from exception import CustomException
from datetime import datetime
from utils import load_config



class DataExtraction:

    def __init__(self):
        config = load_config()
        self.headers = {
            'Accept': 'application/json'
        }    
    def data_extract(self):
        logging.info("Entered the data extraction method") 

        try:
            logging.info(f"Making API call to fetch top posts from {subR} subreddit")
            response = requests.get(f'https://oauth.reddit.com/r/{subR}/top?limit={self.post_limit}&t={self.post_interval}', headers=self.headers)
            
            logging.info(f"Trimming post data")
            response=response.json()
  
        except Exception as e:
                logging.error(f"Error fetching data from Reddit: {e}")
                raise CustomException(e,sys)
            
        try:
            trimmed_data_path = os.path.join('../../../artifacts', self.trimmed_data_filename)
            logging.info(f"Saving to a local json file")
            with open(trimmed_data_path, 'w') as outfile:
                json.dump(self.trimmed_data, outfile, indent=4)
            return trimmed_data_path
        except Exception as e:
            logging.error(f"Error saving file: {e}")
            raise CustomException(e,sys) 
