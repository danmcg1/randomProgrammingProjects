# **Find PI to the Nth Digit** - 
#  Enter a number and have the program generate PI
#   up to that many decimal places.
#  Keep a limit to how far the program will go.
import math

pi=math.pi

i = int(input("Pick a number between 1 and 10: "))

def piToDigit(i):
    """Returns pi to the number generated from i"""
    print(round(pi,i))

piToDigit(i)
