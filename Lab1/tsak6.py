# Task 6: Guess the Number
# Create a program in which the computer randomly selects a number between 1 and 10. The user should keep guessing until the correct number is found.

import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break