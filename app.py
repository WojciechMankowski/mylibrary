from flask import render_template, Flask, request
from Database.mongo import MongoDB
from Helpers.Movie import Movie
from forms import AddItem
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = MongoDB(host="localhost", port=27017)
db.connect_db()

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route("/book/top")
def book_top():
    return render_template("book_top.html")

@app.route("/movie/top")
def movie_top():
    movie = db.find_item()
    return render_template("movie_top.html", movie= movie)

@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    form = AddItem()
    if request.method == "POST" and form.validate_on_submit():
        data = form.data
        movie = Movie(data["title"], data["image"], data["desc"],
                      data["autor"], 1, data["greade"], actors=data["actors"]
                      )

        # print("movie")
        # print(movie)
        db.add_item(data= movie.data_to_json())
        return render_template("add_item.html", form=form, data=movie.data_to_json())
    return render_template("add_item.html", form=form)


if __name__ == '__main__':
    app.run()


# TODO  STWORZYĆ OBRAZ DOCERA
#  TODO  stworzć formularz dodawania nowych rzeczy
#  TODO  stowrzyć formulacz do wystawiania ocen

