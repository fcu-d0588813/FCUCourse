# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:58:52 2018

@author: YURU
"""




import json
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.route("/")
def verify():
    return "Hello world", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    res = {"fulfillmentText": '收到'}
        
    return make_response(jsonify(res))

if __name__ == '__main__':
    app.run(port=5000)