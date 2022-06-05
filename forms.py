from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class AddItem(FlaskForm):
    title = StringField("Tytuł: ", validators=[DataRequired()])
    autor = StringField("Autor: ", validators=[DataRequired()])
    desc = StringField("Opis: ", validators=[DataRequired(), Length(min=10, max=250)])
    image = FileField("Plakatokładka: ", validators=[DataRequired()])
    greade = IntegerField("Twoja ocena: ", validators=[DataRequired()])
