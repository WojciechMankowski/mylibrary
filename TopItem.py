from flask import Blueprint, render_template
from Database.database import SQLLite
top_page = Blueprint("top", __name__, template_folder='templates')

@top_page.route("movie/")
def top_movie():
    db = SQLLite("kultura.db")
    db.connect_db()
    movie = db.FindAllItemSort("Movie")
    return render_template("TopMovie.html", movie=movie)

@top_page.route("book/")
def top_book():
    return render_template("TopBook.html")