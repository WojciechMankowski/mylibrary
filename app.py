import os
from flask import render_template, Flask, request
from forms import AddItem, RateItem
from Database.database import SQLLite
from Helpers.average_grade import CalculateTheAverage
from TopItem import top_page
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(top_page, url_prefix="/top")

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/book")
def book():
    db = SQLLite("kultura.db")
    db.connect_db()
    book = db.FindAllItem("Book")
    return render_template("book_top.html", book=book)


@app.route("/movie")
def movie():
    db = SQLLite("kultura.db")
    db.connect_db()
    movie = db.FindAllItem("Movie")
    return render_template("movie_top.html", movie=movie)


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    form = AddItem()
    if request.method == "POST":
        data = form.data
        db = SQLLite("kultura.db")
        db.connect_db()
        if data["type"] == "Films":
            db.AddItem("Movie",
                   data["title"], data["autor"], data["greade"], 1, data["desc"],
                   data["type"], data["image"], data["actors"]
                   )
        elif data["type"] == "Książka":
            db.AddItem("Book",
                       data["title"], data["autor"], data["greade"], 1, data["desc"],
                       data["type"], data["image"])
        return render_template("add_item.html", form=form)
    return render_template("add_item.html", form=form)


@app.route("/rate/<title>", methods=["GET", "POST"])
def Rate(title: str):
    form = RateItem()
    print(form.RateValidate())
    if request.method == "POST" and form.RateValidate():
        data = form.data
        title = title.replace("_", " ").title()
        db = SQLLite("kultura.db")
        db.connect_db()
        dane = db.FindHow_Grade("Movie", title)
        av = CalculateTheAverage(data["rate"], dane[1], dane[0])
        db.UpdateItem("Movie", av, title, dane[0])
    return render_template("rate.html", title=title, form=form)


if __name__ == '__main__':
    app.run()