"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Name of Pet:", validators=[InputRequired()])
    species = SelectField("Pet Species:",
                          choices=[('cat', "Cat"),
                                   ('dog', "Dog"),
                                   ('porcupine', "Porcupine")],
                          validators=[InputRequired()])
    photo_url = StringField("Photo(URL):", validators=[ Optional(), URL()])
    age = SelectField("Age:",
                      choices=[('baby', "Baby"),
                               ('young', "Young"),
                               ('adult', "Adult"),
                               ('senior', "Senior")], validators=[InputRequired()])
    notes = StringField("Additional Notes: ", validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Form for adding pets """

    photo_url = StringField("Photo(URL):", validators=[URL(), Optional()])
    notes = StringField("Additional Notes: ", validators=[Optional()])
    available = BooleanField("Available: ")
