"""Contains form template for movie upload"""
def get_template():
    """Contains form template"""
    # Styles and scripting for the page
    upload_movies_form = '''
    <span hidden id="upload"></span>
    <form class="form-horizontal" action="/python/cgi-bin/add_movie.py" method="post">
      <div class="form-group">
        <label class="control-label col-sm-2" for="title">Title:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="text" class="form-control" id="title name="title" placeholder="Enter title">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="storyline">Storyline:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="text" class="form-control" id="storyline" name="storyline" placeholder="Enter storyline">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="poster-url">Poster URL:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="text" class="form-control" id="poster-url" name="poster_url" placeholder="Enter poster url">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="youtube-url">Youtube trailer URL:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="text" class="form-control" id="youtube-url" name="youtube_url" placeholder="Enter youtube url">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="rating">Rating:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="text" class="form-control" id="rating" name="rating" placeholder="Rating from 0 - 3">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn-default">Submit</button>
        </div>
      </div>
      <!--
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="button" class="btn btn-default">Regenerate content</button>
        </div>
      </div>
      -->
    </form>
    '''
    upload_movies_template_subparts = {
        "upload_movies_form":upload_movies_form,
        }
    return upload_movies_template_subparts
