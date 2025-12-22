# Create a game to play guessing of numbers

# Define a range for guessing
# You need to ask for guesing number
# conditional check to validate the guess
# Add re-attempting

from random import randint

number = randint(1,5)
user_guess = int(input("Enter your guessed number between 1 - 5: "))
if user_guess == number:
    print("congratulations!!! You have guessed right!!!")
else:
    print(f"Try again, correct number was {number}")