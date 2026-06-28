# **Find PI to the Nth Digit** - 
#  Enter a number and have the program generate PI
#   up to that many decimal places.
#  Keep a limit to how far the program will go.
import random
import math

pi=math.pi

i = random.randint(1,100)

def piToDigit(i):
    """Returns pi to the number generated from i"""
    print(math.trunc(pi,i))

piToDigit(i)

