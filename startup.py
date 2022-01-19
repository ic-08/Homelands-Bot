import datetime
from datetime import *
import pytz
from flask import Flask
from threading import Thread
import time
import requests
from replit import db
import sys
from sys import *
from replit import *
tme = time



#Flask
app = Flask('')
@app.route('/', methods=['GET'])
def home():
    return "Server up"

def run():
  app.run(host='0.0.0.0',port=5000)


def keepalive2():
    iteration = 6
    while True:
        try:
            r = requests.get('https://Pinging-bot.isaacchu1.repl.co/status',timeout=10)
            x = r.json()
            if x[0]['status'] != 'ONLINE' and db['offtime'] == 0:
                print("Bot offline")
                print(f"Bot status : {x[0]['status']}")
                db['offtime'] = tme.time()
            if db['offtime'] != 0 and tme.time() - db['offtime'] > 30 and x[0]['status'] != 'ONLINE':
                print("Rebooting")
                db['offtime'] = 0
                break
            if x[0]['status'] == 'ONLINE' and db['offtime'] != 0:
                db['offtime'] = 0
                
        except:
            pass

        #Time update
        nowtime = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")

        #Reboot at 1 a.m.
        if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) == 1:
            day = datetime.now(pytz.timezone('US/Eastern')).strftime("%B %d ,%Y")
            print(f"Today is {day}") 
            tme.sleep(3600)
            break

        if iteration % 6 == 0:
            print(f"\n\n\n\nAlive as of {nowtime}")
            print(f"Bot status : {str(x[0]['status'])}\n")

        iteration += 1
        tme.sleep(10)

    return






   