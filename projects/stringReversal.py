
def test_function():
    input = "Putting a string in here. Just like this..."
    output = input[::-1]
    # reversed_input = sorted(list(enumerate(input)), key=lambda tup: tup[0], reverse=True)
    # reversed_list = [i[1] for i in reversed_input]
    # output = ''.join(reversed_list)
    
    return(output)

def main():
    print(test_function())


if __name__ == '__main__':
    main()