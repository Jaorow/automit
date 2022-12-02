import random as rand
from flask import Blueprint, redirect, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,SubmitField,TextAreaField, HiddenField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, ValidationError,NumberRange

from better_profanity import profanity

import app.blueprints.services as services
import app.adapters.repository as repo

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def root():
    return render_template("home.html")

@app_blueprint.route('/')
def pg2():
    return render_template("home.html")