"""
Stores the details of the following movies,
and displays the information on a website.
"""
import media
import fresh_tomatoes
"""
Creates movie objects, and initialilzes them with a title, movie poster,
trailer.
"""
ex_machina = media.Movie("Ex Machina", "Robots man.",
                         "https://bit.ly/2jI3RSt",
                         "https://youtu.be/EoQuVnKhxaM")

sinister = media.Movie("Sinister", "Bad things happen.",
                       "http://www.impawards.com/2012/posters/sinister.jpg",
                       "https://youtu.be/_kbQAJR9YWQ")

book_of_life = media.Movie("Book of Life", "Bright colors.",
                           "https://bit.ly/2K3BQAf",
                           "https://youtu.be/_i69CJc1BgE")

smokin_aces = media.Movie("Smokin' Aces", "Shoot em' up.",
                          "https://bit.ly/2I3VEmm",
                          "https://youtu.be/ohhxbsp8Mss")

nightmare_before_christmas = media.Movie("The Nightmare Before Christmas",
                                         "Jack Skellington saves the day.",
                                         "https://bit.ly/2I5ufR3",
                                         "https://youtu.be/wr6N_hZyBCk")

zoolander = media.Movie("Zoolander", "There has to be more too life than being \
                        really reall really rediculously good looking",
                        "http://www.impawards.com/2001/posters/zoolander.jpg",
                        "https://youtu.be/MaEeSJZYkpY")
#Stores movie objects in a list.
movies = [ex_machina, sinister, book_of_life, smokin_aces,
          nightmare_before_christmas, zoolander]
#Opens the movie website in the users browser.
fresh_tomatoes.open_movies_page(movies)
