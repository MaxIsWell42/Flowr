from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import googlemaps
import time
import os

#TODO Finish questions+answers, use google place api to get local restaurants and use answers to query the final page

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Flowr')

# db instantiation
client = MongoClient(host=host)

# Defining the client
gmaps = googlempaps.Client(API_KEY)

# Defaulting to a database
db = client.get_default_database()

# collection names
flowrs = db.flowr
questions = db.question
answers = db.answer

# flask app name
app = Flask(__name__)

# Places API key
API_KEY = AIzaSyC_3HdF4PGrktqWsyzNtGHlv0DDjNqk7Q0

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def flowr_homepage():
    
    if request.method == 'GET':
        return render_template('flowr_hp.html')
    # if request.method == 'POST':
    #     # if there is a post request on the index page
    #     pass

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

@app.route('flowr/<flowr_choice>', methods=['GET'])
def flowr_choice():
    #TODO: implement differenct choices sending you to differnet pages
    if flowr_choice == choice1:
        return render_template('/flowr')
    elif flowr_choice == choice2:
        return render_template('/flowr')

@app.route('flowr/<flowr_id>')
def flowr_final():
""" final page of flowr, where the user can see the final suggestion. Future to include other suggestions and ability to create events """
    return render_template('/flowr/<flowr_id>')

if __name__ == "__main__":
    app.run(debug=True, port=8080)