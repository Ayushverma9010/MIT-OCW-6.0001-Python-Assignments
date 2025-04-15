## 6.100A PSet 1: Part B
## Name: ayush
## Time Spent
## Collaborators:  

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

# User inputs
yearly_salary = float(input("Enter your annual salary: "))  # user's annual salary in dollars
portion_saved = float(input("Enter the portion of salary to save (as a decimal): "))  # portion to save, e.g. 0.1 for 10%
cost_of_dream_home = float(input("Enter the cost of your dream home: "))  # cost of the dream home
semi_annual_raise = float(input("Enter the semi-annual raise (as a decimal): "))  # semi-annual raise as a decimal, e.g., 0.07 for 7%

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# Constants
portion_down_payment = 0.25  # The portion of the home price needed for the down payment (25%)
down_payment = cost_of_dream_home * portion_down_payment  # Amount needed for down payment

# Calculate the monthly savings
monthly_salary = yearly_salary / 12  # Monthly salary
monthly_savings = monthly_salary * portion_saved  # Monthly savings based on portion saved

# Initialize months counter
months = 0
current_savings = 0.0  # Start with zero savings

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

while current_savings < down_payment:
    current_savings += monthly_savings  # Add the monthly savings to the current savings
    months += 1  # Increment the month counter
    
    # Every 6 months, apply the raise
    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise  # Increase salary by the raise percentage
        monthly_salary = yearly_salary / 12  # Recalculate the monthly salary
        monthly_savings = monthly_salary * portion_saved  # Recalculate the savings based on the new salary

# Output the result
print(f"Number of months to save for the down payment: {months}")

