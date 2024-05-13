import sys
import os

current_dir = os.path.dirname(__file__)
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(os.path.abspath(src_dir))

# Import lambda_handler directly
from data_extraction.lambda_function import lambda_handler

print(lambda_handler())