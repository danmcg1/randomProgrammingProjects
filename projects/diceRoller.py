# Dice roller
# Write some code that simulates rolling a number of different dice for a TTRPG
# The code should record the outcomes and display a total.

import random
import sys
import time

all_dice = []
results = []

def dice_to_be_rolled():
    print("\nChoose your dice: Default = d20")
    sides = int(input("d4 | d6 | d8 | d10 | d12 | d20 | d100 |  d")or 20)
    print(f"\nDice selected: d{sides}")
    all_dice.append(sides)

number_of_dice = int(input("How many dice do you want to roll? ").strip() or 1)

def roll_dice(sides):
    return(random.randint(1,sides))

def dice_roller(number_of_dice, sides):
    while(number_of_dice > 0):
        roll = roll_dice(sides)
        results.append(roll)
        number_of_dice -= 1
    
dice_roller(number_of_dice, all_dice)

def rolling_animation():
    start_time = time.time()
    animation_speed = 0.075
    frames = ["|", "/", "—", "\\", "|", "/", "—", "\\"]
    frame_index = 0
    animation_duration = 0.75
    while time.time() - start_time < animation_duration:
        current_frame = frames[frame_index]
        print(f"Rolling... {current_frame}", end="\r")
        sys.stdout.flush()
        frame_index = (frame_index + 1) % len(frames)
        time.sleep(animation_speed)
    print("\r                                    ")

#def sanatised_results(results):
    #clean_results = str(results[0])
    #for i in results[1:]:
    #    clean_results += ", " + str(i)
    #return(clean_results)

def disadvantage_rolls(results):
    return(min(results))

def advantage_rolls(results):
    return(max(results))

rolling_animation()
print(f"\rd{sides} results: {results}\n")
if number_of_dice == 2 and sides == 20:
    print(f"\n\033[92mAdvantage: {advantage_rolls(results)} \n\033[91mDisadvantage: {disadvantage_rolls(results)}\033[0m")
elif sides == 20 and results == [20]:
    print(f"\n\033[93mCRIT: {max(results)}\033[0m")
elif sides == 20 and results == [1]:
    print(f"\n\033[91mFAIL: {max(results)}\033[0m")
elif number_of_dice > 1:
    print(f"\rd{sides} total = {sum(results)}")




