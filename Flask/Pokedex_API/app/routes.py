# app/routes.py

from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Pokemon
from app.forms import PokemonForm
# Import other necessary modules or objects

@app.route('/')
def home():
    return "Welcome to the Pokedex!"

@app.route('/create_pokemon', methods=['GET', 'POST'])  # Allow both GET and POST requests
def create_pokemon():
    form = PokemonForm()
    if form.validate_on_submit():  # Check if the form is submitted and valid
        pokemon = Pokemon(
            name=form.name.data, 
            description=form.description.data, 
            level=form.level.data, 
            cuteness_rating=form.cuteness_rating.data
        )
        db.session.add(pokemon)
        db.session.commit()
        flash('Pokemon created!', 'success')
        return redirect(url_for('view_pokemon', pokemon_id=pokemon.id))
    return render_template('create_pokemon.html', title='Create Pokemon', form=form)

@app.route('/pokemon/<int:pokemon_id>')
def view_pokemon(pokemon_id):
    pokemon = Pokemon.query.get_or_404(pokemon_id)
    return render_template('pokemon.html', title=pokemon.name, pokemon=pokemon)
