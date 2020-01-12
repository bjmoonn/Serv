import requests
import os
import json
import datetime
import time
import phonenumbers
from google.cloud import firestore
from flask import Flask, request, render_template, send_from_directory, session, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, TextAreaField, SubmitField, StringField, IntegerField, FormField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Email
from os import environ
from app import *

class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),InputRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('continue 🡆')

@app.route('/mLogIn', methods=["GET", "POST"])
def merchantLogin_req_get():
    form = LogInForm()
    services = db.collection(u'services').stream()
    if form.validate_on_submit():
        for service in services:
            if service.get('email') == form.email.data and service.get('pass') == form.password.data:
                # return redirect("/tap?service_id=71")
                session['email'] = form.email.data
                return redirect("/merchantManagement?service_id="+service_id)
        return redirect("/tap?service_id=71")
    return render_template("merchantLogIn.html", form=form)
        