
#Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.

def isMultipleOf3(n):
    return (n % 3 == 0)
def isMultipleOf5(n):
    return (n % 5 == 0)
def isMultipleOf15(n):
    return(n % 15 ==0)

for i in range(1, 100):
    if isMultipleOf15(i) == True:
        print(str(i) + "FizzBuzz")
    elif isMultipleOf5(i) == True:
        print(str(i) + "Buzz")
    elif isMultipleOf3(i) == True:
        print(str(i) + 'Fizz')
    else:
        print(i)
    


