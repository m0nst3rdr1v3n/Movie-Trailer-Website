   """Defines the movie class and contains the details of the movies."""
import webbrowser


class Movie():
    """This class stores movie related informationself.
    The attributes are:
    movie_title: which is a string to store the title of the movie.
    movie_storyline: which is a sting to store the description of the movie.
    poster_image: which is a sting to store the url to the movies poster image.
    trailer_youtube: which is a string to store the url to the YouTube traler.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
    #initialilzes movie class.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    #Plays the movie trailer in the web browser.
        webbrowser.open(self.trailer_youtube_url)
