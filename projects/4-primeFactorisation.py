# // **Prime Factorization** - 
# // Have the user enter a number and find all Prime Factors 
# // (if there are any) and display them.

def userSelectNumber():
    selected_number: int = int(input('Select a number: '))
    return selected_number

def primeNumberReturn(selected_number: int):
    factors = []
    n = 2
    # While loop config will search only for the number up to the root of selected_number. Significant performance improvement this way. 
    while n * n <= selected_number:
        while selected_number % n == 0:
            factors.append(n)
            selected_number //= n
        n += 1
    # This if statement is only required when performing the loop on the root of selected number. As in n * n <= selected_number
    if selected_number > 1:
        factors.append(int(selected_number))
    return factors
        

def main():
    selected_number = userSelectNumber()
    print(primeNumberReturn(selected_number))

if __name__ == '__main__':
    main()
