# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:58:52 2018

@author: YURU
"""

import os
import pandas as pd
import psycopg2

#連接資料庫
conn = psycopg2.connect(database="d3l8u727fkdhuh",
                        user="uskhmdlztebice",
                        password="5714697bd569731729daa365947918c513374d064055ec40fd3644ed56963f0f",
                        host="ec2-107-20-237-78.compute-1.amazonaws.com",
                        port="5432")
cursor = conn.cursor()

def get(req):
    p = req['queryResult']['parameters']
    msg = 'Course: ' + p['Course'] + '\nTeacher: ' + p['Teacher'] + '\nAction: ' + p['Action']
	#cursor.execute("SELECT TName from TEACHER where TName='林明言'")
	#rows = cur.fetchall()
    print(msg)
    return msg


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
    
    