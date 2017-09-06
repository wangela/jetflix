import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>JETFLIX</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">

    <!-- Optional JavaScript for Bootstrap 4 -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>

    <style type="text/css" media="screen">
        body {
            background-color:#000;
        }
        h2 {
            color: red;
            font-weight: 800;
        }
        h3 {
            color: #DDD;
            font-size: 150%;
            font-weight: 200;
            text-align: center;
        }
        p.vid-title {
            color: #FFF;
            font-size: 200%;
            font-weight: 200;
            text-align: left;
        }
        .vid-duration {
            color: #FFF;
            font-size: 50%;
            font-weight: 200;
            text-align: left;
        }
        p.vid-storyline {
            color: #FFF;
            font-size: 100%;
            font-weight: 300;
            text-align: left;
        }
        .jumbotron {
            background-color: #000;
            height: 480px;
            padding: 0px;
            margin: 0px;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        #trailerbox {
            border: none;
            height: 360px;
            margin: 0 auto;
            width: 640px;
            background-color: #000;
            z-index: 2;
        }
        #jumbocontainer {
            position: relative;
        }
        #jumbocontainer #infobox {
            position: absolute;
            bottom: 0;
            left: 0;
            border: none;
            margin-left: 0px;
            text-align: left;
            opacity: 0.7;
            width: 400px;
            background-color: #000;
            z-index: 3;
        }
        #detailsbox {
            text-align: left;
            z-index: 4;
        }
        .container-fluid {
            overflow:scroll;
            padding-top: 0px;
        }
        .catalog-row {
            align-content: left;
            display: flex;
            flex-direction: row;
            flex-basis: auto;
            flex-wrap: nowrap;
            margin-left: 30px;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            padding-left: 20px;
            padding-right: 30px;
        }
        .movie-tile:hover {
            background-color: #222;
            cursor: pointer;
        }
        .series-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            padding-left: 20px;
            padding-right: 30px;
        }
        .series-tile:hover {
            background-color: #222;
            cursor: pointer;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Start playing the trailer whenever movie tile is clicked
        $(document).ready(function() {
            $(".movie-tile").click(function() {
                console.log('movie clicked');
                var title = $(this).attr('title');
                var duration = $(this).attr('duration');
                var titlecode = '<div class="container" id="detailsbox"><p class="vid-title">' + title + '&nbsp;&nbsp;<span class="vid-duration">' + duration + '&nbsp;minutes</span></p>'
                var storyline = $(this).attr('storyline');
                var storycode = '<p class="vid-storyline">' + storyline + '</p></div>'
                var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
                var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                console.log(storyline);
                $("#jumbo").css('background-image', 'none');
                $("#infobox").empty().append($(titlecode + storycode));
                $("#trailerbox").empty().append($("<iframe></iframe>", {
                    'id': 'trailer-video',
                    'type': 'text-html',
                    'src': sourceUrl,
                    'frameborder': 0,
                    'allowfullscreen': 'allowfullscreen'
                }));
                $("#trailerbox").css('visibility', 'visible');
            });
            $(".series-tile").click(function() {
                console.log('series clicked');
                var title = $(this).attr('title');
                var seasons = $(this).attr('seasons');
                var titlecode = '<div class="container" id="detailsbox"><p class="vid-title">' + title + '&nbsp;&nbsp;<span class="vid-duration">' + seasons + '&nbsp;seasons</span></p>'
                var storyline = $(this).attr('storyline');
                var storycode = '<p class="vid-storyline">' + storyline + '</p></div>'
                var landscape_url = $(this).attr('landscape-url');
                $("#trailerbox").css('visibility', 'hidden');
                $("#infobox").empty().append($(titlecode + storycode));
                $("#jumbo").css('background-image', 'url(' + landscape_url + ')');
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <!-- Hide navbar
    <div class="container">
      <div class="navbar navbar-expand-md navbar-dark bg-dark fixed-top" role="navigation">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><h2>JETFLIX</h2></a>
          </div>
        </div>
      </div>
    </div>
    -->
    <div class="jumbotron" id="jumbo">
      <div class="container" id="jumbocontainer">
        <h2>JETFLIX</h2>
        <div id="trailerbox">
        </div>
        <div id="infobox">
        </div>
      </div>
    </div>
    <div class="container-fluid">
    <div class="catalog-row">
      {all_tiles}
    </div>
    </div>


  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" title="{movie_title}" duration="{movie_duration}" storyline="{movie_storyline}">
    <img src="{poster_image_url}" width="220" height="342">
    <h3>{movie_title}</h3>
</div>
'''

# A single series entry html template
series_tile_content = '''
<div class="series-tile" landscape-url="{landscape_url}" title="{series_title}" seasons="{series_seasons}" storyline="{series_storyline}">
    <img src="{poster_image_url}" width="220" height="342">
    <h3>{series_title}</h3>
</div>
'''


def create_movie_tiles_content(movies):
    """ Generates movie tiles to be displayed.

    Args:
        movies: A list of media.Movie objects in any order.

    Returns:
        HTML code for a div that displays the movie poster and, when clicked, 
        plays the movie's trailer in the #trailerbox inside the jumbotron 
        at the top of the page.

    """

    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_duration=movie.duration,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def create_series_tiles_content(series):
    """ Generates movie tiles to be displayed.

    Args:
        movies: A list of media.Series objects in any order.

    Returns:
        HTML code for a div that displays the show poster and, when clicked, 
        fills the jumbotron at the top of the page with a high-res landscape 
        image promoting the show.

    """

    content = ''
    for show in series:

        # Append the tile for the show with its content filled in
        content += series_tile_content.format(
            series_title=show.title,
            series_seasons=show.season_count,
            series_storyline=show.storyline,
            poster_image_url=show.poster_image_url,
            landscape_url=show.landscape_url
        )
    return content

def create_all_tiles_content(videos):
    """ Generates tiles for any kind of video to be displayed.

    Args:
        videos: A list of media.Videos objects in any order.

    Returns: 
        HTML for Movie and Series divs (can be mixed together)
        that either play a trailer video or fill the jumbotron 
        with a still image.

    """
    content = ''
    for video in videos:
        if video.media_type == "Movie":
            content += create_movie_tiles_content([video])
        elif video.media_type == "Series":
            content += create_series_tiles_content([video])
    return content

def open_movies_page(movies, shows):
    """ Generates tiles for any kind of video to be displayed.

    Args:
        movies: A list of media.Movies objects in any order.
        shows: A list of media.Shows objects in any order.

    Returns: 
        Generates a new HTML webpage file and opens it in a web browser.

    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    movies_list = sorted(movies, key = lambda movie: movie.title)
    series_list = sorted(shows, key = lambda show: show.title)
    all_list = sorted(movies + shows, key = lambda video: video.title)

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        all_tiles=create_all_tiles_content(all_list))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
