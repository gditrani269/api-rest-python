import json
from flask import Flask, render_template, redirect, request ,jsonify 
#import os
#from flask_swagger_ui import get_swaggerui_blueprint
#from flask_cors import CORS

import psycopg2

conexion1 = psycopg2.connect(host="ec2-23-20-124-77.compute-1.amazonaws.com", database="ddsogo2cmtup33", user="humlprjlvdbdnt", password="f8280465b2f538726d073816c7862c981b13ada9fbd7a0b6813e7ffe620077a6")
cursor1=conexion1.cursor()

app = Flask(__name__)
#cors=CORS(app)
### swagger specific ###


@app.route('/', methods=['GET'])     
def home(): 
    cursor1.execute("SELECT id, name FROM leads")
    sTemp = 'sasa'
    """
    for fila in cursor1:
        print(fila)
        sTemp = sTemp + fila[1] + ' - '
    """
    sOut = "<html><head></head><body>" + sTemp + "</body></html>"
    return sOut
	
	
if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=8081) 
        # app.run(debug=True)
	
	
