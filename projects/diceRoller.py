#**Coin Flip Simulation**
# Write some code that simulates flipping a single coin however many times the user decides.
#  The code should record the outcomes and count the number of tails and heads.

import random

print("\nChoose your dice:")
sides = int(input("d4 | d6 | d8 | d10 | d12 | d20 | d100 |  ")or 20)
print(f"\nDice selected: d{sides}")

number_of_dice = int(input("How many dice do you want to roll? ").strip() or 1)

results = []

def roll_dice(sides):
    return(random.randint(1,sides))

def dice_roller(number_of_dice, sides):
    while(number_of_dice > 0):
        roll = roll_dice(sides)
        results.append(roll)
        number_of_dice -= 1
    
dice_roller(number_of_dice, sides)

print(results)
print(f"Total = {sum(results)}")