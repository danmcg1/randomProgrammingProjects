#Fibonacci Sequence** - 
#Enter a number and have the program generate the Fibonacci sequence 
#to that number or to the Nth number.
import random
position = random.randint(1,20)

position = int(input("What position do you want?: "))

numbers = [0,1]

def fibonacci(position):
    """Finding the fibonacci number at a specific position"""
    if position == 0: 
        print(0)
    elif position == 1:
        print(1)
    else:
        for i in range(position):
            new_number= numbers[0]+numbers[1]
            numbers[0] = numbers[1]
            numbers[1] = new_number
        print(numbers[1])

fibonacci(position)

