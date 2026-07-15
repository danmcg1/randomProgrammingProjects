#Fibonacci Sequence** - 
#Enter a number and have the program generate the Fibonacci sequence 
#to that number or to the Nth number.
import random
position = random.randint(1,20)

position = int(input("What position do you want?: "))

numbers = [1,1]

def fibonacci(position):
    """Appending to the array instead of replacing it"""
    if position == 0:
        print(0)
    elif position == 1:
        print(1)
    else:
        for i in range(position):
            new_number = numbers[i]+numbers[i+1]
            numbers.append(new_number)
            print(numbers[i])

fibonacci(position)

