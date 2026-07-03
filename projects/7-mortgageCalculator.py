# Calculate the MONthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = int(input("What is the mortgage term?: "))
mortgage_term = 28
interest_rate = 4.5
interest_rate_percentage = interest_rate / 100
principle = 240000

interest_interval = "monthly" 
#["yearly","monthly","weekly","daily"]

def interest_rate_in_period():
    if interest_interval == "yearly":
        interest_in_period = interest_rate_percentage 
    elif interest_interval == "monthly":
        interest_in_period = (interest_rate_percentage / 12) 
    elif interest_interval == "weekly":
        interest_in_period = (interest_rate_percentage / 52) 
    elif interest_interval == "daily":
        interest_in_period = (interest_rate_percentage / 365) 
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

r = interest_rate_in_period()
n = number_of_periods()

history = []
current_balance = principle

periodic_payment = principle * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))

for period in range(1, n + 1):
    interest_over_period = current_balance * r
    principle_paid_over_period = periodic_payment - interest_over_period
    ending_balance = current_balance - principle_paid_over_period

    history.append({
        "period": period,
        "starting_balance": current_balance,
        "interest": interest_over_period,
        "principal_paid": principle_paid_over_period,
        "ending_balance": ending_balance
    })

    print(f"Period {period}: Start: £{current_balance:.2f} | Interest: £{interest_over_period:.2f} | End: £{ending_balance:.2f}")
    
    current_balance = ending_balance



