
# Check whether a word is a palindrome with True or False being returned


def isPalindrome(word):
    for n in range(int(len(word)/2)):
        if word[n] != word[-(n+1)]:
            return(False)
        else:
            n += 1
    return(True)

def main():
    word = input(f"Enter a word: ")
    print(isPalindrome(word))

if __name__ == '__main__':
    main()
            
    


