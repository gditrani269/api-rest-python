import json
from flask import Flask, render_template, redirect, request ,jsonify 
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
    
    sOut = "ON"
    return sOut

@app.route('/OFF', methods=['GET'])     
def home2(): 
    print("hola")
    
    sOut = "OFF"
    return sOut
	
if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=8081) 
        # app.run(debug=True)
	
	
