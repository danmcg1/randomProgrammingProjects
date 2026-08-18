
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


bracketPairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}

brackets = [item for pair in bracketPairs.items() for item in pair]



def userInput() -> str:
    value = '[{}](h{e[l]l}o)'
    # value = input(f'Add a string with parentheses: ')
    return value



def getBracketsFromString(stringDict: dict) -> dict:
    allowedKeys = set(brackets)
    filteredDict = [k for k in stringDict if k in allowedKeys]
    return filteredDict




def main():
    input = userInput()
    print (getBracketsFromString(input))
    

if __name__ == '__main__':
    main()