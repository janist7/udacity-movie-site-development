"""Writes new movie json with a new movie"""
import json

def add_new_movie(title, storyline, poster_url, youtube_url, rating):
    """
    Creates new movie dictionary
    Has parameters:
     title
     storyline
     poster_url
     youtube_url
     rating
    """

    new_movie = {"title":title,
                 "storyline":storyline,
                 "poster_image_url":poster_url,
                 "trailer_youtube_url":youtube_url,
                 "rating":rating}
    write_new_file(add_movie_to_dictionary(new_movie))

    return True


def add_movie_to_dictionary(new_movie):
    """Opens movies.json and appends new movie, has one list parameter"""

    with open('movies/movies.json', 'r') as movies_json:
        movies_dictionary = json.load(movies_json)
    movies_dictionary["movies"].append(new_movie)

    return movies_dictionary


def write_new_file(new_movie_dictionary):
    """Writes new movie json file, has one dictionary parameter"""

    with open('movies/movies.json', 'w') as movies_json:
        json.dump(new_movie_dictionary, movies_json)
