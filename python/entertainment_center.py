import media
import fresh_tomatoes_main
import fresh_tomatoes_upload
import json

with open('movies/movies.json') as movies_json:
    movies_dictionary = json.load(movies_json)

movies_list = []
for movie in movies_dictionary["movies"]:
    movies_list.append(media.Movie(movie["title"],
                                   movie["storyline"],
                                   movie["poster_image_url"],
                                   movie["trailer_youtube_url"],
                                   int(movie["rating"])))

fresh_tomatoes_upload.open_upload_movies_page()
fresh_tomatoes_main.open_main_movies_page(movies_list)