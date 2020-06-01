'''
####################
Python video series: First Project
####################
Tasks:
decide how to store movies
movie format?
show UI and get user input
allow users to add movies
allow users to display their movies
allow users to find a movie
allow users to stop program execution
####################
'''

movies = []

def show_ind_movie(movie):
    print(f"Movie: {movie['name'].title()}")
    print(f"Director: {movie['director'].title()}")
    print(f"Year: {movie['year'].title()}")

def add_movie():
    movie = {}
    movie['name'] = input("What is the name of the movie you would like to add?\n").lower()
    movie['director'] = input("Who directed this movie?\n").lower()
    movie['year'] = input("What year was this movie made?\n").lower()
    movies.append(movie)


def find_movie():
    types = ['name', 'director', 'year']
    movie_search_type = False
    found = []
    while movie_search_type == False:
        movie_search_type = input("Would you like to search by Name, Director or Year: ").lower()
        if movie_search_type not in types:
            print(f"{movie_search_type} not a valid choice. \n")
            movie_search_type = False

    movie_search = input(f"Type in the movie {movie_search_type.title()}: ")
    for movie in movies:
        if movie[movie_search_type] == movie_search:
            found.append(movie)

    if found != []:
        for movie in found:
            show_ind_movie(movie)
    else:
        print(f"{movie_search.title()} is not in your list.")


def view_movie():
    for movie in movies:
            show_ind_movie(movie)


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            view_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command - please try again:  ')

        user_input = input("Enter 'a' to add a movie, 'l' to see a movie, 'f' to find a movie, and 'q' to quit: ")


menu()
