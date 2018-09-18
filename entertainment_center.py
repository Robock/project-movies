import media
import fresh_tomatoes
'''Specific instances are structured in this file.
Each movie object and its parameters are organized in such a way that it can be initialized by the 
class Movie from the media module.
The imported fresh_tomatoes module is also used to create the movie website.''' 

monty_python = media.Movie("Monty Python and the Holy Grail",
	"History is turned on its comic head when, in 10th century England, King Arthur travels the countryside to find knights who will join him at the Round Table in Camelot.",
	"http://lsc.mit.edu/schedule/2014.2q/poster-montypythonandtheholygrail.jpg",
	"https://www.youtube.com/watch?v=urRkGvhXc8w")

inconvenient_sequel = media.Movie("An Inconvenient Sequel: Truth to Power",
	"A movie about climate change.",
	"http://www.xfdrmag.net/wp-content/uploads/2017/08/an-inconvenient-sequel-poster.jpg",
	"https://www.youtube.com/watch?v=huX1bmfdkyA")

star_wars = media.Movie("Star Wars: The Force Awakens",
	"A battle between the Resistance and the daunting legions of the First Order.",
	"http://cdn.inquisitr.com/wp-content/uploads/2015/10/star-wars-the-force-awakens-poster.jpg",
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")

the_matrix = media.Movie("The Matrix",
	"Together with Trinity, Neo and Morpheus fight against the machine's enslavement of humanity.",
	"http://2.bp.blogspot.com/-2F8gEE3lENI/UEFvWy-MCLI/AAAAAAAAMkA/P5O9gKXKLbs/s1600/The+Matrix+(1999)+1.jpg",
	"https://www.youtube.com/watch?v=vKQi3bBA1y8")

inception = media.Movie("Inception",
	"A thief, who steals corporate secrets through use of dream-sharing technology.",
	"http://3.bp.blogspot.com/_n7-Pz2d4T-U/TUW9lfRlCMI/AAAAAAAAAFk/RM-EIJOtdZU/s1600/Inception.jpg",
	"https://www.youtube.com/watch?v=8hP9D6kZseM")

napoleon_dynamite = media.Movie("Napoleon Dynamite",
	"Alienated teenager decides to help his new friend win the class presidency in their small western high school.",
	"http://images.moviepostershop.com/napoleon-dynamite-movie-poster-2004-1020250842.jpg",
	"https://www.youtube.com/watch?v=ZHDi_AnqwN4")


movies = [monty_python, inconvenient_sequel, star_wars, the_matrix, inception, napoleon_dynamite]
fresh_tomatoes.open_movies_page(movies)