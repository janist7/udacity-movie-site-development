#!/usr/bin/env python
#!python
"""Generates movie site html pages"""
import json
import media
import fresh_tomatoes_main
import fresh_tomatoes_upload

def get_movies_list():
    """Opens movies json file, returns movie list"""
    with open('movies/movies.json', 'r') as movies_json:
        movies_dictionary = json.load(movies_json)

    movies_list = []
    for movie in movies_dictionary["movies"]:
        movies_list.append(media.Movie(movie["title"],
                                       movie["storyline"],
                                       movie["poster_image_url"],
                                       movie["trailer_youtube_url"],
                                       int(movie["rating"])))
    return movies_list

fresh_tomatoes_upload.write_upload_html()
fresh_tomatoes_main.write_index_html(get_movies_list())
