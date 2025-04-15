## 6.100A PSet 1: Part C
## Name: [Your Name Here]
## Time Spent: [Enter your time spent here]
## Collaborators: [List any collaborators here, or "None" if applicable]

##############################################
## Get user input for initial_deposit below ##
##############################################

# User inputs
initial_deposit = float(input("Enter your initial deposit: "))  # the initial amount saved up
yearly_salary = float(input("Enter your annual salary: "))  # user's annual salary in dollars
portion_saved = float(input("Enter the portion of salary to save (as a decimal): "))  # portion to save
cost_of_dream_home = float(input("Enter the cost of your dream home: "))  # cost of the dream home

# Constants
portion_down_payment = 0.25  # The portion of the home price needed for the down payment (25%)
down_payment = cost_of_dream_home * portion_down_payment  # Amount needed for down payment
monthly_salary = yearly_salary / 12  # Monthly salary
monthly_savings = monthly_salary * portion_saved  # Monthly savings based on portion saved

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# Initialize variables for binary search
low = 0  # low end of the rate of return
high = 1  # high end of the rate of return (100% interest per year)
epsilon = 0.0001  # Accuracy threshold for binary search

# Binary search for the lowest rate of return
while high - low > epsilon:
    guess_rate = (high + low) / 2  # mid point for the guess rate
    current_savings = initial_deposit  # start with the initial deposit
    months = 0  # count the months needed to reach the down payment

    # Simulate the savings process with the current guess rate
    while current_savings < down_payment:
        current_savings += current_savings * (guess_rate / 12)  # apply monthly interest
        current_savings += monthly_savings  # add monthly savings
        months += 1  # increment the month counter

    # Adjust the binary search bounds based on whether we reached the goal
    if current_savings >= down_payment:
        high = guess_rate  # we found a valid rate, try a lower rate
    else:
        low = guess_rate  # we didn't reach the down payment, try a higher rate

# After binary search finishes, `high` will hold the lowest valid rate
print(f"Lowest rate of return (annual) needed: {high * 100:.4f}%")
