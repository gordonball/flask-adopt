"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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
    """ Displays list of pets on main page """

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Displays form for adding new pet, if submitted/validated redirect to home page. """

    form = AddPetForm()
    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes
                      )

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect('/')

    else:
        return render_template('add_pet_form.html',
                               form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """ Displays edit pet form, if submitted/validated redirect to pet info page
        else display 404 error. """

    pet = Pet.query.get_or_404(pet_id)

    # prepopulates form
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data


        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash(f"Edited {pet.name}!")
        return redirect(f"/")
    else:
        return render_template("pet_info.html", pet=pet, form=form)

