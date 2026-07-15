# Calculate the MONthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

### ------------------------------- Loan information ----------------------------
loan_1 = {
    "loan_term": 5,
    "interest_rate": 4.5,
    "principle": 18000,
}

overpayments: int = 100

#["yearly","monthly","weekly","daily"]
interest_interval = "monthly" 

### ------------------------------ Setuo functions -----------------------------
def interest_rate_percentage_conversion(loan_dict: dict):
    interest_rate_percentage = loan_dict["interest_rate"] / 100
    return(interest_rate_percentage)

def interest_rate_in_period(loan_dict):
    if interest_interval == "yearly":
        return interest_rate_percentage_conversion(loan_dict) 
    elif interest_interval == "monthly":
        return (interest_rate_percentage_conversion(loan_dict) / 12) 
    elif interest_interval == "weekly":
        return (interest_rate_percentage_conversion(loan_dict) / 52) 
    elif interest_interval == "daily":
        return (interest_rate_percentage_conversion(loan_dict) / 365) 
    return(0)

def number_of_periods(loan_dict: dict):
    if interest_interval == "yearly":
        n = loan_dict["loan_term"] 
    elif interest_interval == "monthly":
        n =  loan_dict["loan_term"] * 12
    elif interest_interval == "weekly":
        n =  loan_dict["loan_term"]  * 52
    elif interest_interval == "daily":
        n =  loan_dict["loan_term"]  * 365
    return(0)

historic_payments = []

loans = [loan_1]

### --------------------------- Monthly calculations -------------------------------
for loan in loans:
    r = interest_rate_in_period(loan)
    n = number_of_periods(loan)
    current_balance = loan_1["principle"]
    periodic_payment = loan_1["principle"] * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))
    print(f"Total Owed: £{loan["principle"]:.2f}| {interest_interval} overpayment: £{overpayments:.2f} | Bill for period: £{periodic_payment}")

    period = 1
    while current_balance > 0:

        interest_over_period = current_balance * r
        principle_paid_over_period = periodic_payment + overpayments - interest_over_period
        ending_balance = current_balance - principle_paid_over_period

        historic_payments.append({
            "current_balance": current_balance,
            "interest_in_period": interest_over_period,
            "current_balance": current_balance,
        })

        print(f"Month {period}: Start: £{current_balance:.2f} | Interest: £{interest_over_period:.2f} | End: £{ending_balance:.2f}")
        
        current_balance = ending_balance
        period += 1



