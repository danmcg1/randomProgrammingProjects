#**Coin Flip Simulation**
# Write some code that simulates flipping a single coin however many times the user decides.
#  The code should record the outcomes and count the number of tails and heads.

import random

def coin_flip():
    result = random.randint(0,1)
    if result == 0:
        return("H")
    elif result == 1:
        return("T")
    

def flip_calculator(number_of_flips):
    results = []
    for n in range(number_of_flips):
        flip = coin_flip()
        results.append(flip)
    return(results)


def main():
    number_of_flips = int(input("How many coin flips do you want to make? ").strip() or 1)
    results = flip_calculator(number_of_flips)
    print(results)
    print(f"Heads: {results.count('H')} | Tails: {results.count('T')} ")

if __name__ == '__main__':
    main()
