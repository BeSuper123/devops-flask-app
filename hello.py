import redis
import time
import json
from flask import Flask
app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
    data = r.get('/')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] > 600:
            return data['html']
    data = '<p>Welcome!</p> <br> <a href="/about">About Section</a> <br> <a href="/contact">Contact Us</a>'
    r.set('about', json.dumps ({
             'html': data,
             'time': time.time()
    }))
    return data

@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] > 600:
            return data['html']
    data = '<p>The following link is a link to the flask explanation page -></p> <a href="https://flask.palletsprojects.com">Link to flask</a> <br><br><a href="https://python.org">Link to python</a>' # Put your old HTML f-string here!    
    r.set('about', json.dumps ({
         'html': data,
         'time': time.time()
    }))
    return data

@app.route('/contact')
def contact_sec():
    data = r.get('contact')
    if data is not None:
            data = json.loads(data)
            # 600 seconds == 10 minutes
            if time.time() - data['time'] > 600:
                    return data['html']
    data = '<p>My Name: Blessing Ugochukwu <br> My Email: Bugochukwu17@gmail.com</p>'
    r.set('about', json.dumps ({
             'html': data,
             'time': time.time()
    }))
    return data    
