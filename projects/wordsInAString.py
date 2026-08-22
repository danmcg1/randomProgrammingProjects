

def wordsInString(string):
    words = len(string.split())
    return words
    
    

def main():
    string = input(f"Enter a string of your choice: ")
    print(wordsInString(string))

if __name__ == '__main__':
    main()
            
    


