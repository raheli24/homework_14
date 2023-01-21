from flask import Flask, jsonify
from utils import get_by_cast, get_by_title, rating_children, rating_adults,rating_family,get_by_years, get_by_genre

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/movie/<title>")
def get_film_by_title(title):
    film = get_by_title(title)
    return jsonify(film)


@app.route("/movie/<int:year_1>/to/<year_2>")
def get_films_by_years(year_1, year_2):
    films = get_by_years(year_1, year_2)
    return jsonify(films)


@app.route("/rating/children")
def films_for_kids():
    films = rating_children()
    return jsonify(films)


@app.route("/rating/family")
def films_for_family():
    films = rating_family()
    return jsonify(films)


@app.route("/rating/adults")
def films_for_adults():
    films = rating_adults()
    return jsonify(films)


@app.route("/genre/<genre>")
def films_by_genre(genre):
    films = get_by_genre(genre)
    return jsonify(films)


if __name__ == '__main__':
    app.run(debug=True)
