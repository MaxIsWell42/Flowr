from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import time
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Flowr')
client = MongoClient(host=host)
db = client.get_default_database()
flowr = db.flowrs

app = Flask(__name__)

@app.route('/')
def flowr_homepage():
    """homepage"""
    return render_template('flowr_hp.html', flowr=flowr.find())

@app.route('/flowr/new')
def flowr_new():
    """ Where the user creates a flowr chart. """
    return render_template('flowr_new.html', flowr={}, title='New Flowr')
    