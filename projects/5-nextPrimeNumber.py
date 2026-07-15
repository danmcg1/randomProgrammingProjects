# //**Next Prime Number** - 
# // Have the program find prime numbers until the 
# // user chooses to stop asking for the next one.

def userSelectNumber():
    selected_number = int(input('Select a number: '))
    return selected_number

def nextPrimeNumber(selected_number):
    for number in range(1, selected_number):
        if selected_number % number == 0:
            print(number)
        

def main():
    selected_number = userSelectNumber()
    nextPrimeNumber(selected_number)

if __name__ == '__main__':
    main()
