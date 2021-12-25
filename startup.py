import datetime
from datetime import *
import pytz
from flask import Flask
from threading import Thread
import time
import requests
from replit import db
tme = time

#Flask
app = Flask('')
@app.route('/', methods=['GET'])
def home():
    return "Server up"

def run():
  app.run(host='0.0.0.0',port=5000)


def statuscheck():
    while True:
        try:
            r = requests.get('https://Pinging-bot.isaacchu1.repl.co/status',timeout=1000)
            x = r.json()
            print(f"Bot status : {x[0]['status']}")
            if x[0]['status'] != 'ONLINE':
                print("Bot offline")
                system('busybox reboot')
            tme.sleep(10)
        except:
            print("Server down")



def keepalive2():
    while True:
        nowtime = datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M")
        print(f"\n\n\n\nAlive as of {nowtime}")
        tme.sleep(60)

        

def startup():
    t = Thread(target=run)
    t.start()

    t1 = Thread(target=keepalive2)
    t1.start()

    t2 = Thread(target=statuscheck)
    t2.start()


   