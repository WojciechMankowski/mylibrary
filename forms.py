from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SelectField, validators, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class AddItem(FlaskForm):

    title = StringField("Tytuł: ", validators=[DataRequired()])
    autor = StringField("Autor: ", validators=[DataRequired()])
    desc = TextAreaField("Opis: ", validators=[
                         DataRequired(), Length(min=10, max=200)])
    image = FileField("Plakatokładka: ", validators=[validators.Optional()])
    actors = StringField("Actorzy/Gwiazdy w filmie:  ",
                         validators=[validators.Optional()])
    greade = IntegerField("Twoja ocena: ", validators=[DataRequired()])
    type = SelectField("Wybierz rodzaj: ", choices=[
                       "Książka", "Film"], validators=[DataRequired()])
    sumbit = SubmitField("Dodaj")


class RateItem(FlaskForm):
    rate = IntegerField("Twoja ocena: ",
                        validators=[DataRequired()])
    sumbit = SubmitField("Oceń")

    def rate_validate(self):
        if type(self.rate.data) == "int":
            if self.rate.data < 1 or self.rate.data > 10:
                return True
        return False
