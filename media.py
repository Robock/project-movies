import webbrowser
''' This module intitializes instances and plays movie trailers.
In this module, the class Movie has two functions.
The first function, the predefined __init__, initializes the different instances.
The second function, plays movie trailers.'''

class Movie:
	def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
		'''The built-in python function __init__ initializes the different objects.
		The argument movie_title indicates to the title of the movie.
		The argument movie_storyline indicates to the story line of the movie.
		The argument movie_poster indicates to the poster of the movie.
		The argument movie_trailer indicates to the movie trailer.
		The output of this function is specific instances get initialized.'''

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer

	def show_trailer(self):
		'''The function show_trailer plays movie trailers.
		Using the imported module webbrowser, it opens movie_trailer.'''
		webbrowser.open(self.trailer_youtube_url)