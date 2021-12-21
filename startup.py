import datetime
from datetime import *
import pytz
from flask import Flask
from threading import Thread
import time
from replit import db
import json

#Flask
app = Flask('')
@app.route('/')
def home():
   return "Server up"
def run():
  app.run(host='0.0.0.0',port=5000)


tme = time #Define time because it will get mixed up with datetime module
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
   