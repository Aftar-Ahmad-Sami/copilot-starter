from flask import Flask
import time

app = Flask(__name__)

def hello():
    """
    This function returns a greeting message.
    """
    return "Hi, Guys!"

def seconds_since_epoch():
    """
    Returns the number of seconds since the Unix epoch.
    """
    epoch = time.time()
    return str(epoch)

def days_since_epoch():
    """
    Calculate the number of days since the epoch.

    Returns:
        str: The number of days since the epoch.
    """
    epoch = time.time()
    days = epoch / 86400
    return str(days)

@app.route("/")
def seconds():
    """
    This function returns the result of calling the hello() function.
    """
    return hello()

@app.route("/hours")
def hours():
    """
    Returns the number of hours since the epoch.
    
    Returns:
        str: The number of hours since the epoch.
    """
    epoch = time.time()
    hours = epoch / 3600
    return str(hours)

@app.route("/days")
def days():
    """
    Returns the number of days since the epoch.
    """
    return days_since_epoch()

@app.route("/date")
def date():
    """
    Returns the current date and time as a string.
    """
    return time.ctime()

