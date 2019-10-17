from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import time
import os
import googlemaps
import requests

#TODO Finish questions+answers, use answers to query the final page, finish wireframes.

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Flowr')

# db instantiation
client = MongoClient(host=host)

# Defaulting to a database
db = client.get_default_database()

# collection names
flowrs = db.flowr
questions = db.questions
answers = db.answer

# Places API key
API_KEY = os.environ.get('API_KEY')

# Defining the client
gmaps = googlemaps.Client(key=API_KEY)

# flask app name
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET'])
def flowr_homepage():
    if request.method == 'GET':
        #print(details)
        return render_template('index.html')

@app.route('/thai',methods=['GET'])
def thai():
    if request.method == 'GET':
        query = 'Thai resturant'
        return query

@app.route('/mexican', methods=['GET'])
def mexican():
    if request.method == 'GET':
        query = 'Mexican resturant'
        return query

@app.route('/chinese', methods=['GET'])
def chinese():
    if request.method == 'GET':
        query = 'Chinese resturant'
        return query

@app.route('/american', methods=['GET'])
def american():
    if request.method == 'GET':
        query = 'American resturant'
        return query

@app.route('/indian', methods=['GET'])
def indian():
    if request.method == 'GET':
        query = 'Indian resturant'
        return query

@app.route('/japanese', methods=['GET'])
def japanese():
    if request.method == 'GET':
        query = 'Japanese resturant'
        return query

@app.route('/italian', methods=['GET'])
def italian():
     if request.method == 'GET':
        query = 'Thai resturant'
        return query

@app.route('/flowr/new')
def flowr_new():
    """ Where the user creates a flowr chart. """
    return render_template('flowr_new.html', flowr={}, title='New Flowr')

@app.route('/flowr', methods=['POST'])
def flowr_show():
    """ Where the user can submit their fully created flowr """
    flowr = {
        'title': request.form.get('title'),
        'questions': request.form.get('questions'),
        'answers': request.form.get('answers'),
        'created_at': datetime.now()
    }
    flowr_id = flowrs.insert(flowr).inserted_id
    return render_template('flowr_show.html', flowr_id=flowr_id)

@app.route('/flowr/<flowr_choice>', methods=['GET'])
# def flowr_choice():
#     #TODO: implement differenct choices sending you to differnet pages
#     if flowr_choice == choice1:
#         return render_template('/flowr')
#     elif flowr_choice == choice2:
#         return render_template('/flowr')

@app.route('/flowr/results')
def flowr_final(query):
    results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
    for i in range(2):
        for x in range(2):
            photo_id = results['results'][i]['photos'][x]['photo_reference']

    f = open('resturant_photo.jpg', 'wb')
    for chunk in gmaps.places_photo(photo_id, max_width=100):
        if chunk:
            f.write(chunk)
    f.close()
    return render_template('flowr_results.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)