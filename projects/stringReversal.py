
def test_function():
    input = "Putting a string in here. Just like this..."
    input_list = list(enumerate(input))
    reversed = sorted(input_list, key=lambda tup: tup[0], reverse=True)
    for i in reversed:
        reversed_input = []
        reversed_input.append(i[1])   
    output = ''.join([str(s) for s in reversed_input])
    
    return(output)

def main():
    print(test_function())


if __name__ == '__main__':
    main()