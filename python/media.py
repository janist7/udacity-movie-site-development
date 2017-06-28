"""Movie class containing all information a movie might have, also opens link to movie trailer"""
import webbrowser

class Movie(object):
    """
    Movie class containing all information a movie might have, also opens link to movie trailer
    Class takes 5 arguments:
      movie_title
      movie_storyline
      poster_image
      trailer_youtube
      movie_rating
    Class has 1 method:
      show_trailer
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = Movie.VALID_RATINGS[movie_rating]

    def show_trailer(self):
        """Opens trailer in webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
