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
number_of_dice = 1

while dice_type > 0:

    print("\nChoose your dice:")
    dice_type = int(input("d4 | d6 | d8 | d10 | d12 | d20 | d100 |  d").strip() or 0)
    if dice_type == 0:
        print(f"\nDice selected: d20")
    else:
        print(f"\nDice selected: d{dice_type}")

    number_of_dice = int(input("How many dice do you want to roll? ").strip() or 0)
    dice_pool.update({dice_type: number_of_dice})

if dice_pool == {0:0}:
    dice_pool = {20:1}
elif dice_pool == {0:number_of_dice}:
    dice_pool = {20: number_of_dice}

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


def disadvantage_rolls(results):
    return(min(results))

def advantage_rolls(results):
    return(max(results))


rolling_animation()

def all_dice(dice_dict, results_dict):
    for type_of_dice in dice_dict:
        roll_dice_of_type(type_of_dice, dice_dict[type_of_dice])
        if sum(results_dict[type_of_dice]) > 1:
            print(f"\r\nd{type_of_dice} results: {results_dict[type_of_dice]}")
        if dice_dict == {20: 2}:
           print(f"\n\033[92mAdvantage: {advantage_rolls(results_dict[type_of_dice])} \n\033[91mDisadvantage: {disadvantage_rolls(results_dict[type_of_dice])}\033[0m")
        elif type_of_dice == 20 and results_dict[type_of_dice] == [20]:
            print(f"\n\033[93mCRIT: {max(results_dict[type_of_dice])}\033[0m")
        elif type_of_dice == 20 and results_dict[type_of_dice] == [1]:
            print(f"\n\033[91mFAIL: {max(results_dict[type_of_dice])}\033[0m")


all_dice(dice_pool, results_pool)
