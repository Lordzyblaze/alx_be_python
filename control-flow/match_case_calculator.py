"""
Create a Python script named that  will prompt the user to enter
two numbers and select an operation (addition, subtraction, multiplication, or division).
The script will then perform the selected operation using a Match
Case statement and display the result.
"""

#Prompt for User Input
num1 = float(input("enter first number"))

num2 = float(input("enter Second number"))

#Perform the Calculation Using Match Case

operation = input("Choose the operation (+, -, *, /): ")

match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")

#displaying a message if the user tries to divide by zero
    
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please choose one of +, -, *, /.")