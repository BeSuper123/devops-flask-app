from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Welcome!</p> <br> <a href="/about">About Section</a> <br> <a href="/contact">Contact Us</a>'

@app.route('/about')
def about_sec():
	return '<p>The following link is a link to the flask explanation page -></p> <a href="https://flask.palletsprojects.com">Link to flask</a> <br><br><a href="https://python.org">link to python</a>'''

@app.route('/contact')
def contact_sec():
	return '<p>My Name: Blessing Ugochukwu <br> My Email: Bugochukwu17@gmail.com</p>'
	
