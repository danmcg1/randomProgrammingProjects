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

interest_interval = "monthly" 
#["yearly","monthly","weekly","daily"]

### ---------------------------------- Creating basic inputs -------------------------------

def interest_rate_percentage(mortgage_dict):
    interest_rate_as_percentage = mortgage_dict["interest_rate"] / 100
    return(interest_rate_as_percentage)

def interest_rate_in_period(mortgage_dict):
    if interest_interval == "yearly":
        interest_in_period = interest_rate_percentage(mortgage_dict) 
    elif interest_interval == "monthly":
        interest_in_period = interest_rate_percentage(mortgage_dict) / 12
    elif interest_interval == "weekly":
        interest_in_period = interest_rate_percentage(mortgage_dict) / 52 
    elif interest_interval == "daily":
        interest_in_period = interest_rate_percentage(mortgage_dict)  / 365 
    return(interest_in_period)


def number_of_periods():
    if interest_interval == "yearly":
        n = mortgage_term 
    elif interest_interval == "monthly":
        n = mortgage_term * 12
    elif interest_interval == "weekly":
        n = mortgage_term  * 52
    elif interest_interval == "daily":
        n = mortgage_term  * 365
    return(n)

n = number_of_periods()

historic_payments = []

### -------------------------- Functions to set up calculations -------------------------------
def principle(mortgage_dict):
    return(mortgage_dict["principle"])

def starting_balance(mortgage_dict):
    return(mortgage_dict["principle"])

def periodic_payment(mortgage_dict, r, n):
    periodic_payment = mortgage_dict["principle"] * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))
    return(periodic_payment)

def interest_over_period(mortgage_dict, r):
    interest = mortgage_dict["current_balance"] * r
    return(interest)



#### ------------------------------- Performing calculations --------------------------------

for mortgage in my_mortgages:
    mortgage["current_balance"] = starting_balance(mortgage)

for mortgage in my_mortgages:
    for period in range(1, int(n + 1)):

        r = interest_rate_in_period(mortgage)

        start_value = mortgage["current_balance"]

        interest_this_period = interest_over_period(mortgage, r)

        principle_paid_this_period = periodic_payment(mortgage, r, n) - interest_over_period(mortgage, r)

        mortgage["current_balance"] = mortgage["current_balance"] - principle_paid_this_period

        historic_payments.append({
            "period": period,
            "starting_balance": start_value,
            "interest": interest_this_period,
            "principal_paid": principle_paid_this_period,
            "ending_balance": mortgage["current_balance"]
        })

        print(f"Period {period}: Start: £{starting_balance(mortgage):.2f} | Interest: £{interest_this_period:.2f} | End: £{mortgage["current_balance"]:.2f}")
        
        start_value = mortgage["current_balance"]



