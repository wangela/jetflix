import webbrowser

class Video():
	TYPES = ["Movie", "Series"]

	def __init__(self, media_type, title, storyline, poster_url):
		self.media_type = media_type
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_url


class Movie(Video):
	""" This class provides a way to store information about movies. It is a child of class Video. """

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_type, movie_title, movie_storyline, poster_url, duration, trailer_url):
		Video.__init__(self, movie_type, movie_title, movie_storyline, poster_url)
		self.duration = duration
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class Series(Video):
	""" This class provides a way to store information about Series. It is a child of class Video. """

	def __init__(self, show_type, show_title, show_storyline, poster_url, number_of_seasons, landscape_url):
		Video.__init__(self, show_type, show_title, show_storyline, poster_url)
		self.season_count = number_of_seasons
		self.landscape_url = landscape_url
		self.trailer_youtube_url = ""
		self.duration = 0

	def show_details(self):
		print("This show has " + str(self.season_count) + " seasons.")