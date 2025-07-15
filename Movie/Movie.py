class Movie():
    def __init__(self, title, director, duration, watched, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.watched = watched
        self.rating = rating

    def __str__(self):
#if self watched = sum return sum diff

        return f"Movie: {self.title}, directed by {self.director}, Duration: {self.duration} minutes, Status: {self.watched}, Rating: {self.rating}"
    
    def mark_as_watched(self):
        self.watched = True
        rating = float(input("What do you rate this film? "))
        self.rating = rating

        print(self.rating, self.watched )

    
    def is_long_movie(self):
        if (self.duration > 150):
            return True
        else:
            return False
    
    def update_rating(self):
        new_rating = float(input("What is your new rating for this movie? "))
        self.rating = new_rating
        print(self.rating)

    def reset_watch_status(self):
        self.watched = False
        self.rating = "N/A"
        print(self.watched, self.rating)
    

movie = Movie("The Movie", "'Big' John Shlong", 197, False, float(9.5) )




print(movie.is_long_movie())

movie.update_rating()

movie.mark_as_watched()

movie.reset_watch_status()

movie.update_rating()



