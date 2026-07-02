# Calculate the MONthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = int(input("What is the mortgage term?: "))
mortgage_term = 25
interest_rate = 4.5
interest_rate_percentage = interest_rate / 100
principle = 240000

interest_interval = "daily" 
    #["yearly","monthly","weekly","daily"]
    # Yearly = 1
    # Monthly = 12
    # Weekly = 52
    # Daily = 365

initial_balance = principle

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

periodic_payment = principle * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))
interest_over_period = principle * r
principle_paid_over_period = principle - interest_over_period
new_balance_principle = principle - principle_paid_over_period

print(periodic_payment)
print(interest_over_period)
print(principle_paid_over_period)
print(new_balance_principle)

