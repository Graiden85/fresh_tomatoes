# import necessary ancilary files
import media
import fresh_tomatoes

# define details for each
swTFA = media.Movie(
    "Star Wars: The Force Awakens",
    "Three decades after the defeat of the Galactic Empire, a new threat "
    "arises. The First Order attempts to rule the galaxy and only a ragtag "
    "group of heroes can stop them, along with the help of the Resistance.",
    "http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=sGbxmsDFVnE")  # noqa

equilibrium = media.Movie(
    "Equilibrium",
    "In a Fascist future where all forms of feeling are illegal, a man in "
    "charge of enforcing the law rises to overthrow the system.",
    "http://ia.media-imdb.com/images/M/MV5BMTkzMzA1OTI3N15BMl5BanBnXkFtZTYwMzUyMDg5._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=raleKODYeg0")

serenity = media.Movie(
    "Serenity",
    "The crew of the ship Serenity tries to evade an assassin sent to "
    "recapture one of their number who is telepathic.",
    "http://ia.media-imdb.com/images/M/MV5BMTI0NTY1MzY4NV5BMl5BanBnXkFtZTcwNTczODAzMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=JY3u7bB7dZk")
# create array for list
movies = [swTFA, equilibrium, serenity]
# execute pre-written code example
fresh_tomatoes.open_movies_page(movies)
