# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
# Also figure out how long it will take the user to pay back the loan. 
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# mortgage_term = int(input("What is the mortgage term?: "))
mortgage_term = 25
interest_rate = 4.5
interest_rate_percentage = interest_rate / 100
mortgage_initial = 240000

Interest_interval = ["yearly","monthly","weekly","daily"]
    # Yearly = 1
    # Monthly = 12
    # Weekly = 52
    # Daily = 365


for index, item in enumerate(Interest_interval):
    input_message = f'{index + 1}) {Interest_interval}\n'
    

input_message += 'Your choice (enter number or name): '

print("--- Generated Prompt ---")
print(input_message)
print("-----------------------")

# def interest_in_year(period):
    # for interval in period


