#app/mainm.py

from flask import Flask
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        args= request.args
        data = {
            "Modules" : args.get("name"),
            "Subject" : "Data Stbbbbbructures and Algorithms",
        }
  
        return jsonify(data)