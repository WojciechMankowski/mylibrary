from flask import render_template, Flask, request

from Helpers.Movie import Movie
from forms import AddItem
import os
from Database.database import SQLLite
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# db = SQLLite("kultura.db")
# db.connect_db()

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/book")
def book_top():
    return render_template("book_top.html")

@app.route("/movie")
def movie_top():
    db = SQLLite("kultura.db")
    db.connect_db()
    movie = db.FindAllItem("Movie")
    return render_template("movie_top.html", movie= movie)

@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    form = AddItem()
    if request.method == "POST" and form.validate_on_submit():
        data = form.data
        db = SQLLite("kultura.db")
        db.connect_db()
        db.AddItem("Movie",
                    data["title"],data["autor"],data["greade"], 1, data["desc"],
                   data["type"],data["image"], data["actors"]

                    )
        return render_template("add_item.html", form=form, )
    return render_template("add_item.html", form=form)


if __name__ == '__main__':
    app.run()


# TODO  STWORZYĆ OBRAZ DOCERA
#  TODO  stworzć formularz dodawania nowych rzeczy
#  TODO  stowrzyć formulacz do wystawiania ocen

