import json
import pprint

def add_new_movie(title='Test',storyline='Test',poster_url='Test',youtube_url='Test',rating='0'):
    new_movie = {"title":title,
                "storyline":storyline,
                "poster_image_url":poster_url,
                "trailer_youtube_url":youtube_url,
                "rating":rating}
    write_new_file(add_movie_to_dictionary(new_movie))
    return True

def add_movie_to_dictionary(new_movie):
    with open('movies/movies.json', 'r') as movies_json:
        movies_dictionary = json.load(movies_json)
    movies_dictionary["movies"].append(new_movie)
    return movies_dictionary

def write_new_file(new_movie_dictionary):
    with open('movies/movies.json', 'w') as movies_json:
        json.dump(new_movie_dictionary, movies_json)

