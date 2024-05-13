import logging 
import os
from datetime import datetime

#LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y')}.log"

main_project_path = os.path.dirname(os.getcwd())

# Define the path to the logs directory at the main project level
logs_path = os.path.join(main_project_path, "logs")
os.makedirs(logs_path,exist_ok=True) 
# if the director exists, keep appending the file

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

