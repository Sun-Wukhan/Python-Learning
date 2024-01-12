from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class PokemonForm(FlaskForm): 
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Description', validators=[DataRequired(), Length(min=10, max=500)])
    level = IntegerField('Level', validators=[DataRequired()])
    cuteness_rating = IntegerField('Cuteness Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Create Pokemon')