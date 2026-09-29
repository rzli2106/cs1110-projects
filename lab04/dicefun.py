# function that rolls two dice from range of user inputs and returns the sum of the two rolls

import random
def rollem(first,last):
    x = random.randint(first,last)
    y = random.randint(first,last)

    roll = x+y
    return roll
