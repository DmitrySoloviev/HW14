from utils import get_by_title, get_by_year, get_by_rating, get_by_genre
from flask import Flask, render_template, abort
import logging

app = Flask(__name__)


@app.route("/movie/<title>")
def get_movie_title(title):
    logging.info("Страница фильма запрошена")
    movie_by_title = get_by_title(title)
    if movie_by_title is None:
        return abort(404)
    return render_template("movie_by_title.html", movie=movie_by_title)


@app.route("/genre/<genre>")
def get_movie_genre(genre):
    logging.info("Страница фильма по жанрам запрошена")
    movie_by_genre = get_by_genre(genre)
    if movie_by_genre is None:
        return abort(404)
    return render_template("movie_by_genre.html", movies=movie_by_genre)

@app.route("/movies/<rating>")
def get_movie_rating(rating):
    logging.info("Страница фильма по рейтингу запрошена")
    movie_by_rating = get_by_rating(rating)
    if movie_by_rating is None:
        return abort(404)
    return render_template("movie_by_rating.html", movies=movie_by_rating)



@app.route("/movie/<int:year_from>/<int:year_to>")
def get_movie_year(year_from, year_to):
    logging.info("Страница списка фильмов по годам запрошена")
    movie_by_year = get_by_year(year_from, year_to)
    if movie_by_year is None:
        return abort(404)
    return render_template("movie_by_year.html", movies=movie_by_year)


app.run(port=8000, debug=True)