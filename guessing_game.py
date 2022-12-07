"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Pseudo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    user_name = input("What's your name? ")
    print('Welcome to the game,', user_name, '!')

    solution_num = random.randint(1, 100)
    print(solution_num)

    guess_num = int(input('Guess a number from 1-100: '))
    while guess_num != solution_num:
      if guess_num > solution_num:
        guess_num = int(input("It's lower. Guess again: "))
      else:
        guess_num = int(input("It's higher. Guess again: "))
    print('You got it!')


# Kick off the program by calling the start_game function.
start_game()