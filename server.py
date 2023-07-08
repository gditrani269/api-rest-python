import json
from flask import Flask, render_template, redirect, request ,jsonify 


import time
import serial
ser = serial
# configure the serial connections (the parameters differs on the device you are connecting to)
def ini_ser ():
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    ser.isOpen()
    return ser

#import os
#from flask_swagger_ui import get_swaggerui_blueprint
#from flask_cors import CORS

app = Flask(__name__)
#cors=CORS(app)
### swagger specific ###

@app.route('/', methods=['GET'])     
def home(): 
    print("hola")
    
    sOut = "<html><head></head><body>" + "root del server ca toy papa, we do it" + "</body></html>"
    return sOut
	
@app.route('/ON', methods=['GET'])     
def home1(): 
    print("hola")

    ser.write (str.encode('b'))
    sOut = "ON"
    return sOut

@app.route('/OFF', methods=['GET'])     
def home2(): 
    print("hola")

#    ser.isOpen()
    ser.write (str.encode('a'))
    sOut = "OFF"
    return sOut
	

if __name__ == '__main__':
        ser = ini_ser ()
        app.run(debug=True,host='0.0.0.0',port=8081) 
        # app.run(debug=True)
