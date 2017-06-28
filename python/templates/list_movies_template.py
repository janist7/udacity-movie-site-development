"""Contains parts for movie list content"""
#Uses code from this reposatory:
#https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py

def get_template():
    ''' List movies template '''
    # The main page layout and title bar
    main_page_content = '''
      <body>
      <span hidden id="main"></span>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
          <div class="modal-dialog">
            <div class="modal-content">
              <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
              </a>
              <div class="scale-media" id="trailer-video-container">
              </div>
            </div>
          </div>
        </div>
        <!-- Main Page Content -->
        <div class="container">
          {movie_tiles}
        </div>
      </body>
    </html>
    '''
    # A single movie entry html template
    movie_tile_content = '''
    <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <figure>
        <img src="{poster_image_url}" width="220" height="342">
        <span class="{movie_raiting}">{movie_raiting}</span>
        </figure>
        <h2>{movie_title}</h2>
        <p class="storyline-text">{movie_storyline}</p>
    </div>
    '''
    list_movies_template_subparts = {
        "main_page_content":main_page_content,
        "movie_tile_content":movie_tile_content
        }
    return list_movies_template_subparts
