#!flask/bin/python
# -*- coding: utf-8 -*-
from clp3 import clp
from clp_settings import part_of_speech, description

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__)

##########################################################

@app.route('/')
def index():
	return render_template('home.html')

@app.route('results', methods=['POST'])
def results():
	word=request.form['word']
	ids=clp.rec(word)
	words=[]
	for id in ids:
		words.append({
		'label': clp.label(id),
		'base': clp.bform(id), 
		'forms': clp.forms(id),
		'part': part_of_speech[clp.label(id)[0:1]],
		'vec' : clp.vec(id, word)
		})

	return render_template('word.html', word=word, words=words)
#######################################################      

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5011)

