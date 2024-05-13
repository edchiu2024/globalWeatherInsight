import sys 
import logging

def error_message_detail(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message
    

# example of the usage
# Need to import: from logger import *
'''
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e :
        logging.info("Error")
        print(logging.LOG_FILE_PATH)
        raise CustomException(e, sys) 
'''