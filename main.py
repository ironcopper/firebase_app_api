#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify,request
from firebase_utils import *

app = Flask(__name__) 

@app.route('/robot') 
def index():
    latitude = request.args.get('lat') 
    longtitude = request.args.get('lot') 
    ripeness = request.args.get('ripeness') 

    
    saveToDb(latitude, longtitude, ripeness)
    sendTopicMessage(latitude, longtitude, ripeness)

    return jsonify({
        "status":200 #OK/successful 
        
    },
    {
        "lat": latitude, 
        "long": longtitude,
        "ripness":ripeness        
    }
    )

                    
app.run() 