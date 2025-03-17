# Select a random bewteen 10 and 20, let the user to gess the number
# Author Jerry Huang

import random

# Generate a random number between 10 and 20
random_number = random.randint(10, 20)

print("Guess a number between 10 and 20.")

# Loop until the user guesses the correct number
while True:
    # Prompt the user for input
    user_guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number:", random_number)
        break
    else:
        print("Wrong guess. Try again!")
