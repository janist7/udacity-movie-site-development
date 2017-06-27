def get_template():
    '''Contains main template'''
    
    # Styles and scripting for the page
    main_page_head = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Fresh Tomatoes!</title>

        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
        <!-- Roboto -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet">
        <!-- Css/Js -->
        <link rel="stylesheet" href="css/main.css">
        <script src="js/main.js"></script>
    </head>
    '''
    # Page navigation
    main_page_navigation = '''
    <div class="container">
          <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
              <div class="navbar-header">
                <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
              </div>
              <ul class="nav navbar-nav">
                <li class="active"><a class="navbar-nav" href="index.html">Main</a></li>
                <li><a class="navbar-nav" href="fresh_tomatoes_upload.html">Upload Movie</a></li>
              </ul>
            </div>
          </div>
        </div>
    '''
    # Page footer
    main_page_footer = '''
    <footer class="container-fluid bg-4 text-center">
        <p>&copy; Copyright: Janis Tidrikis</p>
    </footer>
    '''
    
    main_template_subparts = {
        "main_page_head":main_page_head,
        "main_page_navigation":main_page_navigation,
        "main_page_footer":main_page_footer
        }
    return main_template_subparts