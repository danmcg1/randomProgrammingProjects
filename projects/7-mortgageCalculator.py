# Calculate the  payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = float(input("What is the mortgage term?: ") or 26.8)
mortgage_term: float = 26.8
overpayments: int = 0


mortgage_1 = {
    "principle": 150649.88,
    "interest_rate": 3.08,
}

mortgage_2 = {
    "principle": 87843.20,
    "interest_rate": 4.69,
}

my_mortgages = [mortgage_1, mortgage_2]

interest_intervals = {
        "yearly": 1,
        "monthly": 12,
        "weekly": 52,
        "daily": 365,
    }

def get_interest_interval() -> str:

    interest_interval_choices = list(interest_intervals.keys())
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


def period_constants(mortgage_dict: dict, interest_interval: str):
    rate_as_pct = mortgage_dict["interest_rate"] / 100

    if interest_interval in interest_intervals:
        multiplier = interest_intervals[interest_interval]
        return [rate_as_pct / multiplier, mortgage_term * multiplier]

    return [0.0, 0.0]


### -------------------------- Calculation Functions -------------------------------

def starting_balance(mortgage_dict: dict):
    return mortgage_dict["principle"]

def periodic_payment(mortgage_dict: dict, r: float, n: int):
    if r == 0:
        return mortgage_dict["principle"] / n
    payment = mortgage_dict["principle"] * ((r * pow(1 + r, n)) / (pow(1 + r, n) - 1))
    return payment

def interest_over_period(mortgage_dict: dict, r: float):
    return mortgage_dict["current_balance"] * r


def all_calculations(overpayment):
### --------------------------------- Calculations on mortgage total  ---------------------------------
    combined_total_owed = 0.0
    combined_periodic_payment = 0.0
    total_interest_paid = 0.0
    total_principle_paid = 0.0

    for mortgage in my_mortgages:
        mortgage["current_balance"] = starting_balance(mortgage)
        
        r, n = period_constants(mortgage, interest_interval)
        payment = periodic_payment(mortgage, r, n)
        
        combined_total_owed += mortgage["principle"] 
        combined_periodic_payment += payment

### ------------------------------- Calculations for each period -----------------------------------
    for period in range(1, int(n + 1)):

        payment_details = []
        combined_interest_this_period = 0.0
        combined_principle_paid_this_period = 0.0
        combined_remaining_balance = 0.0

        for mortgage in my_mortgages:
            interest_this_period = interest_over_period(mortgage, r)
            
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
            total_interest_paid += combined_interest_this_period
            total_principle_paid += combined_principle_paid_this_period

        if combined_remaining_balance <= 0:
            break
        if overpayment <= 0:
            print(f"Year {period // 12} Month {(period % 12) +1} | Remaining Owed: £{combined_remaining_balance:10.2f} | Combined Interest: £{combined_interest_this_period:7.2f} |")
    print(f"| Initial Total Owed: £{combined_total_owed:,.2f} | Bill per period: £{combined_periodic_payment:,.2f}\n ")


    totals = {
    "total_interest_paid": total_interest_paid,
    "total_principle_paid": total_principle_paid
              }
    return totals


def all_calculations_with_overpayments(overpayment):
    if overpayment <= 0:
        return
### --------------------------------- Calculations on mortgage total  ---------------------------------
    combined_total_owed = 0.0
    combined_periodic_payment = 0.0
    total_interest_paid = 0.0
    total_principle_paid = 0.0

    for mortgage in my_mortgages:
        mortgage["current_balance"] = starting_balance(mortgage)
        
        r, n = period_constants(mortgage, interest_interval)
        payment = periodic_payment(mortgage, r, n)
        
        combined_total_owed += mortgage["principle"] 
        combined_periodic_payment += payment

### ------------------------------- Calculations for each period -----------------------------------
    for period in range(1, int(n + 1)):

        payment_details = []
        combined_interest_this_period = 0.0
        combined_principle_paid_this_period = 0.0
        combined_remaining_balance = 0.0

        for mortgage in my_mortgages:
            interest_this_period = interest_over_period(mortgage, r)
            
            mortgage_payment = periodic_payment(mortgage, r, n)
            principle_paid_this_period = mortgage_payment + (overpayment/2) - interest_this_period

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
            total_interest_paid += combined_interest_this_period
            total_principle_paid += combined_principle_paid_this_period

        if combined_remaining_balance <= 0:
            break
        if overpayment > 0:
            print(f"Year {period // 12} Month {(period % 12) +1} | Remaining Owed: £{combined_remaining_balance:10.2f} | Combined Interest: £{combined_interest_this_period:7.2f} |")
    print(f"| Initial Total Owed: £{combined_total_owed:,.2f} | Bill per period: £{(combined_periodic_payment + overpayment):,.2f}\n ")

    totals = {
    "total_interest_paid": total_interest_paid,
    "total_principle_paid": total_principle_paid
              }
    return totals


def main():
    overpayment = 0

    results = all_calculations(overpayment)
    total_payment = results["total_interest_paid"] + results["total_principle_paid"]

    if overpayment > 0:
        results_with_overpayment = all_calculations_with_overpayments(overpayment)
        total_payment_with_overpayment = results_with_overpayment["total_interest_paid"] + results_with_overpayment["total_principle_paid"]
        
        interest_saved = results["total_interest_paid"] - results_with_overpayment["total_interest_paid"]
        print(f"| Interest saved with overpayments: £{interest_saved:,.2f}")
        print(f"| Total payment: £{total_payment:,.2f} ")
        print(f"| Total paid with overpayments: £{total_payment_with_overpayment:,.2f}")
        
if __name__ == '__main__':
    main()
