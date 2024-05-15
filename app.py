from flask import Flask
import time

app = Flask(__name__)

def hello():
    return "Hi, Guys!"

def seconds_since_epoch():
    epoch = time.time()
    return str(epoch)

def days_since_epoch():
    epoch = time.time()
    days = epoch / 86400
    return str(days)

@app.route("/")
def seconds():
    return hello()

@app.route("/hours")
def hours():
    epoch = time.time()
    hours = epoch / 3600
    return str(hours)

@app.route("/days")
def days():
    return days_since_epoch()

@app.route("/date")
def date():
    return time.ctime()

