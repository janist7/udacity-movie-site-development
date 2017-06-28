import cgi, cgitb
import update_movies_json

cgitb.enable(display=0, logdir="python/log")
form = cgi.FieldStorage(
    fp=self.rfile,
    headers=self.headers,
    environ={'REQUEST_METHOD':'POST'}
    )
title = form.getvalue('title')
storyline = form.getvalue('storyline')
poster_url = form.getvalue('poster_url')
youtube_url = form.getvalue('youtube_url')
rating = form.getvalue('rating')

if(update_movies_json.add_new_movie(title,storyline,poster_url,youtube_url,rating)):
    print("Movie json updated")
else:
    print("Error")
