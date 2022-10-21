"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class AddPetForm(FlaskForm):
    """ """
    name = StringField("Name of Pet:")
    species = StringField("Pet Species:")
    photo = StringField("Photo(URL):")
    age = SelectField("Age:",
                choices = [('baby', "Baby"),
                           ('young', "Young"),
                           ('adult', "Adult"),
                           ('senior', "Senior")]
    )
    notes = StringField("Additional Notes:")
