# //**Next Prime Number** - 
# // Have the program find prime numbers until the 
# // user chooses to stop asking for the next one.
import math

def userSelectNumber():
    selected_number = int(input('Select a number: '))
    return selected_number

def isPrimeNumber(number: int):
    if number < 2:
        return False
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True

def nextPrimeNumber(selected_number: int):
    number = selected_number
    while isPrimeNumber(number) == False:
        isPrimeNumber(number)
        number += 1
    return number


def main():
    selected_number = userSelectNumber()
    print(nextPrimeNumber(selected_number))

if __name__ == '__main__':
    main()
