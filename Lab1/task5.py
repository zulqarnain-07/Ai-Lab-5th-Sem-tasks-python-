# Task 5: Simple Movie Recommendation System
# Create a program that asks the user to select a preferred movie genre and recommends a movie.

genre = input("Enter your preferred genre: ").lower()

if genre == "action":
    print("Recommended movie: Top Gun")
elif genre == "comedy":
    print("Recommended movie: Home Alone")
elif genre == "horror":
    print("Recommended movie: The Conjuring")
elif genre == "science fiction":
    print("Recommended movie: Interstellar")
else:
    print("Sorry, no recommendation available.")