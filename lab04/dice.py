"""
A simple die roller

Author: Richard Li rl998
Date: 9/1/2026"""

import random
f = input("Type the first number: ")
first = int(f)

l = input("Type the last number: ")
last = int(l)
x = random.randint(first,last)
y = random.randint(first,last)

roll = x+y
print("Choosing two numbers between " + str(first) + " and " + str(last) + ".")
print("The sum is " + str(roll) + ".")
