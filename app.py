from flask import Flask, render_template, request
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

import json

import parser
import clean

@app.route('/')
def hello_world():
	return render_template('app.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/parse', methods=['POST'])
def parse():
	text = request.form["text"]
	cleaned = clean.clean(text)
	return json.dumps({'output': parser.parse(cleaned[0]), 'pairs': cleaned[1]})

if __name__ == '__main__':
	app.run()