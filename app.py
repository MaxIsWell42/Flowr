from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import time
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Flowr')
# db instantiation
client = MongoClient(host=host)

db = client.get_default_database()
# collection name
flowrs = db.flowr
# flask app name
app = Flask(__name__)

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

@app.route('/flowr')
def flowr_show():
    """ Where the user can submit and see their fully created flowr """
    flowr = {
        'title': request.form.get('title'),
        'questions': request.form.get('questions'),
        'answers': request.form.get('answers'),
        'created_at': datetime.now()
    }
    flowr_id = flowrs.insert(flowr).inserted_id
    return render_template('flowr_show.html', flowr_id=flowr_id)


if __name__ == "__main__":
    app.run(debug=True, port=8080)