"""Writes fresh_tomatoes_upload.html file"""
import templates.template_main as template_main
import templates.upload_movies_template as upload_movies_templat

template = {}
template.update(template_main.get_template())
template.update(upload_movies_templat.get_template())

def write_upload_html():
    """Writes fresh_tomatoes_upload.html file"""
    # Create or overwrite the output file
    output_file = open('../fresh_tomatoes_upload.html', 'w')

    # Output the file
    output_file.write(template["main_page_head"] +
                      template["main_page_navigation"] +
                      template["upload_movies_form"] +
                      template["main_page_footer"])
    output_file.close()
