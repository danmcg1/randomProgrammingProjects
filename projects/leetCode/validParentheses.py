
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
    value = '[](h{e[l]l}o)'
    # value = input(f'Add a string with parentheses: ')
    return value



def bracketCheck(bracketsInString: list) -> list:
    bracketBuffer = []
    try:
        for i in bracketsInString:
            if i == '(':
                bracketBuffer.append(i)
            if i == '{':
                bracketBuffer.append(i)
            if i == '[':
                bracketBuffer.append(i)
            if i == ')':
                bracketBuffer.remove('(')
            if i == '}':
                bracketBuffer.remove('{')
            if i == ']':
                bracketBuffer.remove('[')
    except:
        return(False)
    if bracketBuffer == []:
        return(True)
    else:
        return(False)


def removePairedBracket(input: str) -> bool:
    if input == '(':
        return(True)
    elif input == '{':
        return(True)
    elif input == '[':
        return(True)
    else:
        return(False)

def main():
    input = userInput()
    print(bracketCheck(input))
    

if __name__ == '__main__':
    main()