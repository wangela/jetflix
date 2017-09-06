import webbrowser


class Video():
	""" This class provides a way to store information about videos.

	Attributes:
		media_type: A string indicating whether this video is a "Movie" or "Series".
		title: A string of the video's title.
		storyline: A string containing the synopsis of the video's plot.
		poster_url: A string containing the URL of an image promoting the video in portrait orientation.

	"""

	TYPES = ["Movie", "Series"]

	def __init__(self, media_type, title, storyline, poster_url):
		self.media_type = media_type
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_url


class Movie(Video):
	""" This class provides a way to store information about movies. It is a child of class Video. 

	Attributes:
		title: A string of the movie's title.
		storyline: A string containing the synopsis of the movie's plot.
		poster_url: A string containing the URL of an image promoting the movie in portrait orientation.
		duration: An integer indicating the length of the movie in minutes.
		trailer_url: A string containing the URL of a YouTube video of the movie's trailer.

	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_url, duration, trailer_url):
		Video.__init__(self, "Movie", movie_title, movie_storyline, poster_url)
		self.duration = duration
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		""" Opens a new browser window and plays the YouTube trailer video. """
		webbrowser.open(self.trailer_youtube_url)


class Series(Video):
	""" This class provides a way to store information about Series. It is a child of class Video. 

	Attributes:
		title: A string of the show's title.
		storyline: A string containing the synopsis of the show's plot.
		poster_url: A string containing the URL of an image promoting the show in portrait orientation.
		duration: An integer indicating the number of seasons existing for this show.
		landscape_url: A string containing the URL of a high-res image promoting the show in landscape orientation.

	"""

	def __init__(self, show_title, show_storyline, poster_url, number_of_seasons, landscape_url):
		Video.__init__(self, "Series", show_title, show_storyline, poster_url)
		self.season_count = number_of_seasons
		self.landscape_url = landscape_url
		self.trailer_youtube_url = ""
		self.duration = 0

	def show_details(self):
		""" Prints the number of seasons that the show has. """
		print("This show has " + str(self.season_count) + " seasons.")