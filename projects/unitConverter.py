
# Unit converter: Take units of each type and convert them from Imperial to Metric, or Metric to Imperial
# Additionally build a UI to make it easier to use

conversion_rates = {
    ( "Miles" , "Kilometers" ): 1.60934,
    ( "Kilometers" , "Miles" ): 0.624371,
    ( "Pounds", "Kilograms" ): 0.453592,
    ( "Kilograms", "Pounds" ): 2.20462,
    ( "Inches", "Centimeters"): 2.54,
    ( "Centimeters", "Inches" ): 0.393701
}

def conversions_to_string(tuple) -> str:
    for val in tuple:
        result += str(val) + ' '
    result = result.strip()
    return(result)

def get_conversion_type():
    user_input = ''

    input_message = "Pick an option:\n"

    options = conversions_to_string(conversion_rates.keys())

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    print('You picked: ' + options[int(user_input) - 1])



def unit_convertion(value, conversion) -> float:
    converted_unit = value * conversion
    return(converted_unit)


def get_user_input() -> tuple:
    conversion = get_conversion_type()
    value = float(input(f"How many units?: "))
    return((conversion, value))


def main() -> float:
    print(get_user_input())
    # conversion_result = value * conversion
    # return(conversion_result)

if __name__ == "__main__":
    main()