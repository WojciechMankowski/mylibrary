from flask import render_template, Flask

from Database.mongo import MongoDB

app = Flask(__name__)
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
    return render_template("add_item.html")
if __name__ == '__main__':
    app.run()


# TODO  STWORZYĆ OBRAZ DOCERA
#  TODO  stworzć formularz dodawania nowych rzeczy
#  TODO  stowrzyć formulacz do wystawiania ocen

