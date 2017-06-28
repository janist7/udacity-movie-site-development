"""Gets POST info from fresh_tomatoes_upload.hhml form"""
import cgi
import cgitb
import update_movies_json

"""Todo - looks like i need to rewrite code using flask to get desired result,
posibly flask not useble with github pages"""
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

# Check if json file was updated
if update_movies_json.add_new_movie(title, storyline, poster_url, youtube_url, rating):
    print "Movie json updated"
else:
    print "Error"
