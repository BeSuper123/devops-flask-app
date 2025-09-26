from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a flask app!</p> <br> <a href="/about">About Section</a>'

@app.route('/about')
def about_sec():
	return 'The following link is a link to the flask explanation page -> <a href="https://flask.palletsprojects.com">Link</a>'
