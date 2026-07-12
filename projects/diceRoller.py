#**Dice roller**
# Write some code that simulates rolling a number of different dice for a TTRPG
#  The code should record the outcomes and display a total.

import random
import sys
import time

dice_pool = {}
results = []
results_pool = {}
dice_type = 1

while dice_type > 0:

    print("\nChoose your dice:")
    dice_type = int(input("d4 | d6 | d8 | d10 | d12 | d20 | d100 |  d")or 0)
    print(f"\nDice selected: d{dice_type}")

    number_of_dice = int(input("How many dice do you want to roll? ").strip() or 1)
    dice_pool.update({dice_type: number_of_dice})


def dice_roll(type_of_dice):
    return(random.randint(1,type_of_dice))

def roll_dice_of_type(type_of_dice, number_of_dice):
    rolls = []
    while number_of_dice > 0:
        single_roll = dice_roll(type_of_dice)
        rolls.append(single_roll)
        number_of_dice -= 1
    results_pool.update({type_of_dice: rolls})
        

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

#results = [20]

rolling_animation()

def all_dice(dice_dict, results_pool):
    for type_of_dice in dice_dict:
        roll_dice_of_type(type_of_dice, dice_dict[type_of_dice])
        
        print(f"\r\nd{type_of_dice} results: {results_pool[type_of_dice]}")
        if dice_dict[type_of_dice] == 2 and type_of_dice == 20:
           print(f"\n\033[92mAdvantage: {advantage_rolls(results)} \n\033[91mDisadvantage: {disadvantage_rolls(results)}\033[0m")
        elif type_of_dice == 20 and results == [20]:
            print(f"\n\033[93mCRIT: {max(results)}\033[0m")
        elif type_of_dice == 20 and results == [1]:
            print(f"\n\033[91mFAIL: {max(results)}\033[0m")
        elif type_of_dice > 1:
            print(f"\rd{type_of_dice} total = {sum(results_pool[type_of_dice])}")


all_dice(dice_pool, results_pool)
