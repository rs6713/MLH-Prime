from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from random import randint

import threading
app = Flask(__name__)


import RPi.GPIO as GPIO
import time
freq=10  
colours=[]

@app.route('/')
def display():
    #if request.method == 'POST':
        #jsdata = request.form['javascript_data']
        #return json.loads(jsdata)[0]
        #return render_template('main.html', sam=5);
       # return render_template('sent.html', data=jsdata);
    return render_template('main.html', sam=3);

@app.route('/post', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    return jsdata

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['TEMPLATES_AUTO_RELOAD']=True

#colours=[]
counter=0;
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinLayouts=[{"r":4, "g":2, "b":3, "gnd":6},
{"r":27, "g":17, "b":22, "gnd":9},
{"r":15, "g":23, "b":18, "gnd":9},
{"r":7, "g":8, "b":25, "gnd":20},
{"r":10, "g":9, "b":11, "gnd":25}


]
GPIO.setup(18,GPIO.OUT)

def lightLeds():
    global counter
    count=counter%len(colours)
    for led in range(len(colours[count])):
        #every led 
        if(colours[count][led]=="red"):
            GPIO.output(pinLayouts[led]["r"], GPIO.HIGH)
            GPIO.output(pinLayouts[led]["g"], GPIO.LOW)
            GPIO.output(pinLayouts[led]["b"], GPIO.LOW)
        elif(colours[count][led]=="blue"):
            GPIO.output(pinLayouts[led]["r"], GPIO.LOW)
            GPIO.output(pinLayouts[led]["g"], GPIO.HIGH)
            GPIO.output(pinLayouts[led]["b"], GPIO.LOW)
        elif(colours[count][led]=="green"):
            GPIO.output(pinLayouts[led]["r"], GPIO.LOW)
            GPIO.output(pinLayouts[led]["g"], GPIO.LOW)
            GPIO.output(pinLayouts[led]["b"], GPIO.HIGH)
    counter=counter+1
    threading.Timer(1, lightLeds).start()

  

if __name__ == "__main__":
  lightLeds()
  app.run(host='127.0.0.1', port=8080, debug=True)
