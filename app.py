from flask import Flask, render_template, request
import pickle
import sqlite3
import os
import json

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/classifier.pkl'), 'rb'))

def classify(features):
	label = {1: 'good client', 2: 'bad client'}
	y = clf.predict(features)[0]
	proba = round(clf.predict_proba(features)[0][1]*100, 3)
	return label[y], proba

app_arij = Flask(__name__)

@app_arij.route('/', methods=['GET','POST'] )
def hello_world():
    input= request.json
    classofClient,default=classify(input.get('input'))
    data_set= {'class':classofClient,'defaultProba':default,'input': input.get('input') }
    json_dump=json.dumps(data_set)
    return json_dump
    
