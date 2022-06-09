from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SelectField, validators, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class AddItem(FlaskForm):
    title = StringField("Tytuł: ", validators=[DataRequired()])
    autor = StringField("Autor: ", validators=[DataRequired()])
    desc = TextAreaField("Opis: ", validators=[DataRequired(), Length(min=10, max=200)])
    image = FileField("Plakatokładka: ", validators=[validators.Optional()])
    actors =StringField("Actorzy/Gwiazdy w filmie:  ", validators=[validators.Optional()])
    greade = IntegerField("Twoja ocena: ", validators=[DataRequired()])
    type = SelectField("Wybierz rodzaj: ", choices=["Książka", "Film"], validators=[DataRequired()])
    sumbit = SubmitField("Dodaj")