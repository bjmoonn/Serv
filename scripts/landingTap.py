import requests
import os
import json
import datetime
import time
from flask import Flask, request, render_template, send_from_directory, session, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, TextAreaField, SubmitField, StringField, IntegerField, FormField
from wtforms.validators import DataRequired, InputRequired
from os import environ
from app import *

class PhoneNumberForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[DataRequired(),InputRequired()])
    area_code = IntegerField('Area Code', validators=[DataRequired(), InputRequired()])
    number = IntegerField('Number', validators=[DataRequired(), InputRequired()])

class EnterQueueForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone_number = FormField(PhoneNumberForm)
    submit = SubmitField('Enter Queue')

@app.route("/tap", methods=['GET', 'POST'])
def landingTap_req_get():
    form = EnterQueueForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, phone number {}'.format(
            form.name.data, form.phone_number.data))
        return redirect(url_for('confirmation'))
    return render_template("landingTap.html", form=form)