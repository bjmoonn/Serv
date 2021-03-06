import requests
import os
import json
import datetime
import time
import werkzeug
from google.cloud import firestore
from flask import Flask, request, render_template, send_from_directory, session, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired
from os import environ

if not os.path.isfile("serv-91a70-ab6c2718a3d6.json"):
    f = open("serv-91a70-ab6c2718a3d6.json",'w')
    f.write(environ['serviceData'])
    f.close()


db = firestore.Client(project="serv-91a70")
# db = firestore.Client(project="serv-91a70-ab6c2718a3d6.json")

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

app.secret_key = '\xf0"b1\x04\xe0.[?w\x0c(\x94\xcdh\xc1yq\xe3\xaf\xf2\x8f^\xdc'
firebaseProjectID = environ['PROJECT_ID']
firebaseAPIKey = environ['API_KEY']
twilioAuth = environ['TWILIO_AUTH']
from scripts import confirmation, lineStatus, payment, services, landingTap, merchantSignUp, merchantLogin, merchantManagement, index, verification, merchantAirtable

# Begin send assets
@app.route('/assets/img/<path>')
def send_assets(path):
    return send_from_directory('assets/img', path)


@app.route('/assets/css/<path>')
def send_style(path):
    return send_from_directory('assets/css', path)


@app.route('/assets/js/<path>')
def send_js(path):
    return send_from_directory('assets/js', path)

# End send assets

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return render_template('error.html')

@app.errorhandler(404) 
def handle_bad_request(e):
    return render_template('error.html')