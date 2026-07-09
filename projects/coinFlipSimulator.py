#**Coin Flip Simulation**
# Write some code that simulates flipping a single coin however many times the user decides.
#  The code should record the outcomes and count the number of tails and heads.

import random

number_of_flips = int(input("How many coin flips do you want to make? ").strip() or 1)

# heads = 0
# tails = 0

results = []

def coin_flip():
    result = random.randint(0,1)
    if result == 0:
        return("Heads")
    elif result == 1:
        return("Tails")
    

def flip_calculator(number_of_flips):
    while(number_of_flips > 0):
        flip = coin_flip()
        results.append(flip)
        number_of_flips -= 1

flip_calculator(number_of_flips)

print(results)
print(f"Heads: {results.count('Heads')} | Tails: {results.count('Tails')} ")
