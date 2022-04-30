import datetime
from datetime import *
import pytz
from flask import Flask
import time
from replit import db
tme = time



#Flask
app = Flask('')
@app.route('/', methods=['GET'])
def home():
    return "Server up"

def run():
  app.run(host='0.0.0.0',port=5000)


def timeupdate():
    #Time update
    nowtime = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")

    #Reboot at 1 a.m.
    if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) == 1:
        day = datetime.now(pytz.timezone('US/Eastern')).strftime("%B %d ,%Y")
        print(f"Today is {day}") 
        if datetime.now(pytz.timezone('US/Eastern')).weekday() == 0:
            db['restartctx'] = "reboot"
            
        tme.sleep(3600)
        return "restart"

    try:
        print(f"\n\n\nAlive as of {nowtime}")
    except:
        pass
        
    return





   