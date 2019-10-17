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

# Defining the client
key = os.environ.get('API_KEY')
gmaps = googlemaps.Client(key=key)

# flask app name
app = Flask(__name__)

# Places API key
API_KEY = os.environ.get('API_KEY')

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
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/mexican', methods=['GET'])
def mexican():
    if request.method == 'GET':
        query = 'Mexican resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/chinese', methods=['GET'])
def chinese():
    if request.method == 'GET':
        query = 'Chinese resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/american', methods=['GET'])
def american():
    if request.method == 'GET':
        query = 'American resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/indian', methods=['GET'])
def indian():
    if request.method == 'GET':
        query = 'Indian resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/japanese', methods=['GET'])
def japanese():
    if request.method == 'GET':
        query = 'Japanese resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

@app.route('/italian', methods=['GET'])
def italian():
    if request.method == 'GET':
        query = 'Italian resturant'
        results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)
        photo_id = results['results'][0]['photos'][0]['photo_reference']
        print(photo_id)
        #gmaps.places_photo(photo_id)
        f = open('resturant_photo.jpg', 'wb')
        for chunk in gmaps.places_photo(photo_id, max_width=100):
            if chunk:
                f.write(chunk)
        f.close()
        return results

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
def flowr_choice():
    #TODO: implement differenct choices sending you to differnet pages
    if flowr_choice == choice1:
        return render_template('/flowr')
    elif flowr_choice == choice2:
        return render_template('/flowr')

@app.route('/flowr/<flowr_id>')
def flowr_final():
    return render_template('/flowr/<flowr_id>')

if __name__ == "__main__":
    app.run(debug=True, port=8080)