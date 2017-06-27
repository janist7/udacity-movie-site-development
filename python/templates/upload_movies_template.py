def get_template():
    '''Contains main template'''
    
    # Styles and scripting for the page
    upload_movies_form = '''
    <span hidden id="upload"></span>
    <form class="form-horizontal">
      <div class="form-group">
        <label class="control-label col-sm-2" for="email">Title:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="email" class="form-control" id="email" placeholder="Enter email">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="pwd">Storyline:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <textarea class="form-control" id="email" placeholder="Enter email"></textarea>
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="pwd">Poster URL:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="email" class="form-control" id="email" placeholder="Enter email">
        </div>
      </div>
      <div class="form-group">
        <label class="control-label col-sm-2" for="pwd">Youtube trailer URL:</label>
        <div class="col-lg-9 col-md-9 col-sm-9">
          <input type="email" class="form-control" id="email" placeholder="Enter email">
        </div>
      </div>
      <div class="form-group"> 
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn-default">Submit</button>
        </div>
      </div>
    </form>
    '''
    
    upload_movies_template_subparts = {
        "upload_movies_form":upload_movies_form,
        }
    return upload_movies_template_subparts