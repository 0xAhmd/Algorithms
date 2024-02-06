#implementing Guess Game using Binary Search !

import random

def binary_search_guess_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Initialize the lower and upper bounds
    lower_bound = 1
    upper_bound = 100
    
    # Start the guessing loop
    while True:
        # Calculate the midpoint
        guess = (lower_bound + upper_bound) // 2
        
        # Ask the user to guess the number
        print("Is the number {}?".format(guess))
        response = input("Enter 'l' if the number is lower, 'h' if the number is higher, or 'c' if the guess is correct: ").strip().lower()
        
        # Check the user's response
        if response == 'c':
            print("Yay! I guessed the number {}!".format(guess))
            break
        elif response == 'l':
            # Update the lower bound
            lower_bound = guess + 1
        elif response == 'h':
            # Update the upper bound
            upper_bound = guess - 1
        else:
            print("Invalid input. Please enter 'l', 'h', or 'c'.")

# Start the game
binary_search_guess_game()
