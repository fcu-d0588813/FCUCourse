# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:58:52 2018

@author: YURU
"""

import os
import pandas as pd

def get(req):
    #p = req['queryResult']['parameters']
    
    #msg = 'Course: ' + p['Course'] + '\nTeacher: ' + p['Teacher'] + '\nAction: ' + p['Action']
    
    #print(msg)
    return "接收"


from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.route("/")
def verify():
    return "FCU Course", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    res = {"fulfillmentText": get(req)}
        
    return make_response(jsonify(res))
	
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    