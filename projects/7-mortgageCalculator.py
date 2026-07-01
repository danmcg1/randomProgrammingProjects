# Calculate the MONthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = int(input("What is the mortgage term?: "))
mortgage_term = 25
interest_rate = 4.5
interest_rate_percentage = interest_rate / 100
mortgage_initial = 240000

interest_interval = "daily" 
    #["yearly","monthly","weekly","daily"]
    # Yearly = 1
    # Monthly = 12
    # Weekly = 52
    # Daily = 365

gross_remaining = mortgage_initial
payments = int(input("What are the monthly payments?: "))


def calculate_interest_in_period():
    if interest_interval == "yearly":
        interest_in_period = interest_rate_percentage * float(gross_remaining)
    elif interest_interval == "monthly":
        interest_in_period = (interest_rate_percentage / 12) * float(gross_remaining)
    elif interest_interval == "weekly":
        interest_in_period = (interest_rate_percentage / 52) * float(gross_remaining)
    elif interest_interval == "daily":
        interest_in_period = (interest_rate_percentage / 365) * float(gross_remaining)
    return(interest_in_period)

for i in range(1,mortgage_term):
    new_balance = gross_remaining + calculate_interest_in_period() - payments
    return(new_balance)
    #if new_balance == 0:
     #   break


print("Interest in period = £" + str(calculate_interest_in_period()))
print(new_balance)
