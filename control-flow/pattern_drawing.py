# pattern_drawing.py
# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate the input

while size % 2 == 0:
    #print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

    # Draw the pattern
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

