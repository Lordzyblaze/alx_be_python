# input current age
current_age = int(input("Enter your current age: "))

# input current year
current_year = int(input("Enter the current year: "))

# input specific future year
future_year = int(input("Enter a specific future year: "))

# Calculating future age
future_age = current_age + (future_year - current_year)

# print the result
print(f"In the year {future_year}, you will be {future_age} years old.")
