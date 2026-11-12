"""
A module the plays a coin flip contest.

The player and the opponent take turns guessing a coin flip. The first player
to the goal number of correct guesses wins. If both players reach the guess
at the same time, the players tie.  The player gets to see the opponent's guess
before guessing.

Author: Walker M. White
Date:   November 8, 2026
"""
import random


# The goal to play towards
TARGET_SCORE  = 5


def play(target):
    """
    Plays a single game of coin flip guessing.
    
    The first person with target correct guess wins. The opponent guesses first,
    meaning the player gets to see the opponent's guesses.

    Parameter target: The target score to win the game
    Precondition: target is an int > 0
    """
    player = 0
    other  = 0
    sides = ['H','T']
    names = {'H':'Heads','T':'Tails'}
    
    while player < target and other < target:
        print('Current score is player '+str(player)+'; opponent '+str(other)+'.')
        coin = random.choice(sides)
        opponent = random.choice(sides)
        
        print('The coin has flipped')
        print('The opponent guesses '+names[opponent]+'.')
        response = prompt('What is your guess: (H)eads or (T)ails?: ',('H', 'T'))
        print('The coin is '+names[coin])
        print()
        
        if opponent == coin:
            other += 1
        if response == coin:
            player += 1
    
    print('Final score is player '+str(player)+'; opponent '+str(other)+'.')
    if other >= target and player >= target:
        print('The game is a tie.')
    elif other >= target:
        print('The opponent wins')
    else:
        print('The player wins')


def prompt(prompt,valid):
    """
    Returns the choice from a given prompt.
    
    This function asks the user a question, and waits for a response.  It checks
    if the response is valid against a list of acceptable answers.  If it is not
    valid, it asks the question again. Otherwise, it returns the player's answer.
    
    Parameter prompt: The question prompt to display to the player
    Precondition: prompt is a string
    
    Parameter valid: The valid reponses
    Precondition: valid is a tuple of strings
    """
    # Ask the question for the first time.
    response = input(prompt)
    
    # Continue to ask while the response is not valid.
    while not (response in valid):
        print('Invalid response.  Answer must be one of '+str(valid))
        print()
        response = input(prompt)
    
    return response


# Script code
if __name__ == '__main__':
    play(TARGET_SCORE)
