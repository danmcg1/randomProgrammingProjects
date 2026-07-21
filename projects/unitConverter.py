
# Unit converter: Take units of each type and convert them from Imperial to Metric, or Metric to Imperial
# Additionally build a UI to make it easier to use


conversion_rates = {
    "mi -> km" : 1.60934,
    "km -> mi" : 0.624371,
    "lbs -> kg": 0.453592,
    "kg -> lbs": 2.20462,
    "in -> cm": 2.54,
    "cm -> in": 0.393701
}


def get_conversion_type() -> str:
    user_input = ''

    input_message = "Pick an option:\n"

    options = list(conversion_rates.keys())

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    conversion = options[int(user_input) - 1]
    print('You picked: ' + conversion)
    return(conversion)


def get_user_input() -> tuple:
    conversion = get_conversion_type()
    value = float(input(f"How many units?: "))
    return((conversion, value))

def unit_convertion(value, conversion) -> float:
    multiplier = conversion_rates[conversion]
    converted_unit = value * multiplier
    return(converted_unit)

def main() -> float:
    conversion = get_user_input()
    print(unit_convertion(conversion[1], conversion[0]))

if __name__ == "__main__":
    main()