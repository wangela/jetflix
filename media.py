import webbrowser

class Video():
	def __init__(self, title, storyline, poster_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_url


class Movie(Video):
	""" This class provides a way to store information about movies. It is a child of class Video. """

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_url, trailer_url):
		Video.__init__(self, movie_title, movie_storyline, poster_url)
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	""" This class provides a way to store information about TV Shows. It is a child of class Video. """

	def __init__(self, show_title, show_storyline, poster_url, number_of_seasons):
		Video.__init__(self, show_title, show_storyline, poster_url)
		self.season_count = number_of_seasons

	def show_details(self):
		print("This show has " + str(self.season_count) + " seasons.")