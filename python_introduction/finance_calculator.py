"""
Prompt the user for their monthly income: “Enter your monthly income
Ask for their total monthly expenses: “Enter your total monthly expenses
"""

mincome = float(input ("Enter monthly income"))
mexpenses = float(input ("Enter monthly Expenses"))

msavings = mincome - mexpenses

"""
Assume a simple annual interest rate of 5%.
Calculate the projected savings after one year, incorporating the interest. Use the simplified
formula for annual savings projection: (Projected Savings = Monthly Savings * 12 +
(Monthly Savings * 12 * 0.05)) 
"""
ysavings = (msavings * 12)

yinterest = (msavings * 12* 0.05)

projectedsavings = (ysavings + yinterest)

"""
Display the user’s monthly savings and expenses
Display the projected annual savings after including interest.
"""

print(f" monthly income: {mincome} \nmonthly expenses: {mexpenses} \nprojected annual savings including interest is {ysavings}")

