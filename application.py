# required file for AWS Elastic Beanstalk 
from flask import Flask,request,render_template ,send_from_directory 
#from flask_cors import CORS

import sys
import pandas as pd
from src.pipeline.read_pipeline import ReadPipeline

from src.exception import CustomException

application=Flask(__name__, static_folder='./react_build', static_url_path='/')
app=application  
#CORS(app)



## Route

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/export')
def data_export():
    read_pipeline=ReadPipeline()
    results=read_pipeline.read()
    return results
        

if __name__=="__main__":
    app.run(host="0.0.0.0")    
    

