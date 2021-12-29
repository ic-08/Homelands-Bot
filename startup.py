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
    iteration = int(list(str(datetime.now(pytz.timezone('US/Eastern')).strftime("%M")))[1])
    while True:
        r = requests.get('https://Pinging-bot.isaacchu1.repl.co/status',timeout=10)
        x = r.json()
        print(f"Bot status : {x[0]['status']}")
        if x[0]['status'] != 'ONLINE' and db['offtime'] == 0:
            print("Bot offline")
            db['offtime'] = tme.time()
        if db['offtime'] != 0 and tme.time() - db['offtime'] > 30 and x[0]['status'] != 'ONLINE':
            print("Rebooting")
            db['offtime'] = 0
            break

        #Time update
        nowtime = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")

        #Reboot at 1 a.m.
        if int(datetime.now(pytz.timezone('US/Eastern')).strftime("%H")) == 1:
            day = datetime.now(pytz.timezone('US/Eastern')).strftime("%B %d ,%Y")
            print(f"Today is {day}") 
            tme.sleep(3600)
            break

        roundnumber = list(str(iteration))
        if int(roundnumber[len(roundnumber)-1]) == int(list(str(datetime.now(pytz.timezone('US/Eastern')).strftime("%M")))[1]):
            iteration += 1
            print(f"\n\n\n\nAlive as of {nowtime}")

        tme.sleep(10)

    sys.exit()







   