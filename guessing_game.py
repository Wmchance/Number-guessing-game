"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import median
from statistics import mode
from statistics import mean

high_score = 0
scores_list = []

user_name = input("Enter player name: ")
print(f'Welcome to the game, {user_name}! \U0001f44b')

def start_game(high_score):
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

    print(f"Current High Score: {high_score}")

    solution_num = random.randint(1, 100)

    attempts = []
    guess_num = False

    while guess_num != solution_num:
      try:
        if guess_num == False:
          guess_num = int(input('Guess a number from 1-100: '))
          if guess_num > 100 or guess_num < 1:
            guess_num = False
            raise Exception
        elif guess_num > solution_num and guess_num <= 100:
          guess_num = int(input("It's lower. Guess again: "))
          if guess_num > 100 or guess_num < 1:
            guess_num = attempts[-1]
            raise Exception
        elif guess_num < solution_num:
          guess_num = int(input("It's higher. Guess again: "))
          if guess_num > 100 or guess_num < 1:
            guess_num = attempts[-1]
            raise Exception
      except ValueError:
        print('Sorry, only numbers can be guessed')
      except Exception:
         print('Guess must be between 1 & 100')
      else:
        attempts.append(guess_num)
    
    print('You got it!')
    print(f'Attempts: {len(attempts)}')
    scores_list.append(len(attempts))

    play_again = input('Would you like to play again(Y/N)? ')
    if play_again.lower() == 'y':
      if len(attempts) < high_score or high_score == 0:
        start_game(len(attempts))
      else: 
        start_game(high_score)
    else:
      print('Goodbye! Come play again soon \U0001f600')
      print(f'Score mean: {mean(scores_list)}')
      print(f'Score median: {median(scores_list)}')
      print(f'Score mode: {mode(scores_list)}')


# Kick off the program by calling the start_game function.
start_game(high_score)