import requests
import os
import json
import datetime
import time
import timeit
from flask import Flask, request, render_template, send_from_directory, session, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired
from os import environ
from app import *
from scripts.lineStatus import remindSMSConfirm

services_list = db.collection(u'services')

class ConfirmationForm(FlaskForm):
    submit = SubmitField('i\'m here!')

@app.route("/confirmation", methods=['GET','POST'])
def confirmation_req():
    customerID = request.args['customer_id']
    serviceID = request.args['service_id']
    form = ConfirmationForm()
    if form.validate_on_submit():
        user = services_list.document(serviceID).collection("customers").document(customerID)
        user.delete()
        remindSMSConfirm(serviceID)

        return redirect("/")
    return render_template('confirmation.html', form=form)

