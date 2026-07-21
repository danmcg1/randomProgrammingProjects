# Calculate the  payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = int(input("What is the mortgage term?: "))
mortgage_term = 26.8

mortgage_1 = {
    "principle": 150649.88,
    "interest_rate": 3.08,
}

mortgage_2 = {
    "principle": 87843.20,
    "interest_rate": 4.69,
}

my_mortgages = [mortgage_1, mortgage_2]

def get_interest_interval() -> str:

    interest_interval_choices = ("yearly","monthly","weekly","daily")
    user_input = ''

    input_message = "Pick an option:\n"

    options = interest_interval_choices

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    interest_interval = options[int(user_input) - 1]
    print('You picked: ' + interest_interval)
    return(interest_interval)

interest_interval = get_interest_interval()
### ---------------------------------- Creating basic inputs -------------------------------

def interest_rate_percentage(mortgage_dict: dict):
    interest_rate_as_percentage = mortgage_dict["interest_rate"] / 100
    return(interest_rate_as_percentage)

def interest_rate_in_period(mortgage_dict: dict, interest_interval):
    # Returns the rate directly instead of assigning to a global variable
    rate_as_pct = interest_rate_percentage(mortgage_dict)
    if interest_interval == "yearly":
        return rate_as_pct
    elif interest_interval == "monthly":
        return rate_as_pct / 12
    elif interest_interval == "weekly":
        return rate_as_pct / 52 
    elif interest_interval == "daily":
        return rate_as_pct / 365 
    return 0.0

def number_of_periods(interest_interval):
    if interest_interval == "yearly":
        return mortgage_term 
    elif interest_interval == "monthly":
        return mortgage_term * 12
    elif interest_interval == "weekly":
        return mortgage_term * 52
    elif interest_interval == "daily":
        return mortgage_term * 365
    return 0

n = number_of_periods(interest_interval)


### -------------------------- Calculation Functions -------------------------------

def starting_balance(mortgage_dict: dict):
    return mortgage_dict["principle"]

def periodic_payment(mortgage_dict: dict, r: float, n: int):
    # Basic protection against division by zero if interest rate is 0
    if r == 0:
        return mortgage_dict["principle"] / n
    payment = mortgage_dict["principle"] * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))
    return payment

def interest_over_period(mortgage_dict: dict, r: float):
    return mortgage_dict["current_balance"] * r

#### ------------------------------- Performing calculations --------------------------------

# Initialize the current balance for each mortgage
for mortgage in my_mortgages:
    mortgage["current_balance"] = starting_balance(mortgage)

combined_total_owed = sum(m["principle"] for m in my_mortgages)
combined_periodic_payment = sum(periodic_payment(m, interest_rate_in_period(m,interest_interval), n) for m in my_mortgages)

print(f"Initial Total Owed: £{combined_total_owed:.2f} | Bill for period: £{combined_periodic_payment:.2f}\n")

### ------------------------------- Calculations for each period -----------------------------------
for period in range(1, int(n + 1)):

    payment_details = []
    combined_interest_this_period = 0.0
    combined_principle_paid_this_period = 0.0
    combined_remaining_balance = 0.0

    for mortgage in my_mortgages:
        # Calculate r dynamically for THIS specific mortgage
        r = interest_rate_in_period(mortgage, interest_interval)

        interest_this_period = interest_over_period(mortgage, r)
        
        # Calculate payment based on this mortgage's specific rate
        mortgage_payment = periodic_payment(mortgage, r, n)
        principle_paid_this_period = mortgage_payment - interest_this_period

        mortgage["current_balance"] -= principle_paid_this_period
        
        combined_interest_this_period += interest_this_period
        combined_principle_paid_this_period += principle_paid_this_period
        combined_remaining_balance += mortgage["current_balance"]

        payment_details.append({
            "period": period,
            "interest_this_period": interest_this_period,
            "principle_paid_this_period": principle_paid_this_period,
            "remaining_balance": mortgage["current_balance"],
        })

    print(f"Period {period:3d} | Remaining Owed: £{combined_remaining_balance:10.2f} | Combined Interest: £{combined_interest_this_period:7.2f} |")




