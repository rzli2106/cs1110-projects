"""
A module the plays a coin flip contest.

This is a class-based version of the module flip1.py

<YOUR NAME HERE>
<DATE HERE>
"""
import random


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


class GuessFlip(object):
    """
    A class representing a coin-flipping guessing game.
    
    The game has a set target. The first player to reach that target of correct
    guesses wins the game. The opponent guesses first. The human player gets
    to see the opponent's guess before making their own guess.
    """
    # MUTABLE ATTRIBUTE (GETTERS AND SETTERS)
    # Attribute _target: The target to reach
    # Invariant: _target is an int > 0
    
    # IMMUTABE ATTRIBUTES (GETTERS, BUT NO SETTERS)
    # Attribute _playerScore: The number of correct player guesses
    # Invariant: _playerScore is an int >= 0
    #
    # Attribute _opponentScore: The number of correct opponent guesses
    # Invariant: _opponentScore is an int >= 0

    # CLASS ATTRIBUTE
    TARGET_SCORE  = 5

    # GETTERS AND SETTERS
    def getTarget(self):
        """
        Returns the current guess target
        """
        return self._target
    
    def setTarget(self, value):
        """
        Sets the current guess target
        
        Parameter value: The new guessing target
        Precondition: value is an int > 0
        """
        assert isinstance(value,int) and value > 0
        self._target = value
    
    def getPlayerScore(self):
        """
        Returns the current player score
        """
        return self._playerScore
    
    def getOpponentScore(self):
        """
        Returns the current opponent score
        """
        return self._opponentScore
    
    # INITIALIZER
    def __init__(self, target=TARGET_SCORE):
        """
        Initialize the coin-flipping game with the given target
        
        Parameter target: The goal target to reach
        Precondition: target is an int > 0 (Default TARGET_SCORE)
        """
        self._target = target
        self._playerScore = 0
        self._opponentScore = 0
        
    
    # OTHER METHODS
    def reset(self): # MODIFY HEADER AS NEEDED
        """
        Resets the scores so we can play again
        """
        self._playerScore = 0
        self._opponentScore = 0
    
    def play(self): # MODIFY HEADER AS NEEDED
        """
        Plays a single game of coin flip guessing.
        
        This method runs until either the player or the opponent reaches the
        target. Use the getters to determine the winner when the game completes.
        """

        sides = ['H','T']
        names = {'H':'Heads','T':'Tails'}
        
        while self._playerScore < self._target and self._opponentScore < self._target:
            print('Current score is player '+str(self._playerScore)+'; opponent '+str(self._opponentScore)+'.')
            coin = random.choice(sides)
            opponent_guess = random.choice(sides)
            
            print('The coin has flipped')
            print('The opponent guesses '+names[opponent_guess]+'.')
            response = prompt('What is your guess: (H)eads or (T)ails?: ',('H', 'T'))
            print('The coin is '+names[coin])
            print()
            
            if opponent_guess == coin:
                self._opponentScore += 1
            if response == coin:
                self._playerScore += 1



def main():
    """
    This is the main function for this game.
    
    Most applications have a main entry-point -- a function that starts the
    application. As our game is now a class, not a function, we need to add
    a function to create the game object and run it.
    """
    game = GuessFlip()
    game.play()
    
    player = game.getPlayerScore()
    other  = game.getOpponentScore()
    
    print('Final score is player '+str(player)+'; opponent '+str(other)+'.')
    if other >= game.getTarget() and player >= game.getTarget():
        print('The game is a tie.')
    elif other >= game.getTarget():
        print('The opponent wins')
    else:
        print('The player wins')


# Script code
if __name__ == '__main__':
    main()