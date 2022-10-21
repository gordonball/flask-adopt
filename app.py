"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """ """

    pets = Pet.query.all()

    return render_template('pet_list.html',
        pets=pets
    )


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Form for addding new pet"""
    form = AddPetForm()
    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name, species, photo, age, notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect('/')

    else:
        return render_template('add_pet_form.html',
            form=form)

