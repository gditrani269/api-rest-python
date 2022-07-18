import json
from flask import Flask, render_template, redirect, request ,jsonify 
import os
import requests
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

import psycopg2

conexion1 = psycopg2.connect(host="localhost", database="mi_base", user="postgres", password="cerveza2022")
cursor1=conexion1.cursor()

app = Flask(__name__)
cors=CORS(app)
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Devops - Apisdesk"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])     
def home(): 
    sTemp = 'sasa'
"""
    cursor1.execute("SELECT id, name FROM leads")
    for fila in cursor1:
        print(fila)
        sTemp = sTemp + fila[1] + ' - '
""" 
    sOut = "<html><head></head><body>" + sTemp + "</body></html>"
    return sOut
	
	
if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=80) 
        # app.run(debug=True)
	
	
