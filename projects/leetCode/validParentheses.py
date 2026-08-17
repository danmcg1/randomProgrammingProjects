
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
brackets = ['(','{','[',']','}',')']
openingBrackets = ['(','{','[']
closingBrackets = [')','}',']']
bracketsInString = {}

def userInput() -> str:
    value = input(f'Add a string with parentheses: ')
    return value


def enumerateInput(input) -> dict:
    for location, letter in enumerate(list(input)):
        bracketsInString.update({letter: location})
    return bracketsInString




def onlyBracketsFromString(stringDict: dict) -> dict:
    allowedKeys = set(brackets)
    filteredDict = {k: v for k,v in stringDict.items() if k in allowedKeys}
    return filteredDict

def getBracketLocations(input: str) -> dict:
    return onlyBracketsFromString(enumerateInput(input))



def main():
    input = userInput()
    print (getBracketLocations(input))
    

if __name__ == '__main__':
    main()