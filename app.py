from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import time
import os
import googlemaps
import requests
from pprint import pprint

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
        return redirect(url_for('flowr_final', query=query))

@app.route('/mexican', methods=['GET'])
def mexican():
    if request.method == 'GET':
        query = 'Mexican resturant'
        return redirect(url_for('flowr_final', query=query))

@app.route('/chinese', methods=['GET'])
def chinese():
    if request.method == 'GET':
        query = 'Chinese resturant'
        return redirect(url_for('flowr_final', query=query))

@app.route('/american', methods=['GET'])
def american():
    if request.method == 'GET':
        query = 'American resturant'
        return redirect(url_for('flowr_final', query=query))

@app.route('/indian', methods=['GET'])
def indian():
    if request.method == 'GET':
        query = 'Indian resturant'
        return redirect(url_for('flowr_final', query=query))

@app.route('/japanese', methods=['GET'])
def japanese():
    if request.method == 'GET':
        query = 'Japanese resturant'
    return redirect(url_for('flowr_final', query=query))

@app.route('/italian', methods=['GET'])
def italian():
     if request.method == 'GET':
        query = 'Italian resturant'
        return redirect(url_for('flowr_final', query=query))

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

@app.route('/flowr/results/<query>')
def flowr_final(query):
    results = gmaps.places(query, radius=2, location=['37.773972', '-122.431297'], language='English', max_price=4)

    photo_ids = {}
    _id = 0
    for restaurant in results['results']:
        # print(_id, restaurant)
        photo_ids[_id] = restaurant
        _id += 1

    # photo_ids.append(results['results'][i]['photos'][x]['photo_reference'])
    # for a, b in results['results'].items():
    #     print('a', a)
    #     print('b', b)

    for photo_id, restaurant in photo_ids.items():
        print(photo_id)
        photos = restaurant['photos']
        meta_data = photos[0]
        reference = meta_data['photo_reference']

        with open('/photos/resturant_photo_'+ str(photo_id) + '.jpg', 'wb') as f:
            for chunk in gmaps.places_photo(reference, max_width=100):
                if chunk:
                    f.write(chunk)
        f.close()
    return render_template('flowr_results.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)