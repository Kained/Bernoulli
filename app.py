from flask import Flask, render_template, request
app = Flask(__name__)

import json

import parser

@app.route('/')
def hello_world():
	return render_template('app.html')

@app.route('/parse', methods=['POST'])
def parse():
	text = request.form["text"]
	return json.dumps({'output': parser.parse(text)})

if __name__ == '__main__':
	app.run()