import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function for floor division
def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x // y

# Function for modulus
def modulus(x, y):
    return x % y

# Function for exponentiation (x^y)
def exponentiate(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    return math.sqrt(x)

# Function to calculate factorial of a number
def factorial(x):
    if x < 0:
        return "Error! Factorial is not defined for negative numbers."
    else:
        return math.factorial(int(x))

# Function to calculate logarithm
def logarithm(x):
    if x <= 0:
        return "Error! Logarithm is not defined for zero or negative numbers."
    else:
        return math.log(x)

# Function to calculate sine
def sine(x):
    return math.sin(math.radians(x))

# Function to calculate cosine
def cosine(x):
    return math.cos(math.radians(x))

# Function to calculate tangent
def tangent(x):
    return math.tan(math.radians(x))

# Function to calculate power of 10
def power_of_ten(x):
    return 10 ** x

# Function to calculate natural logarithm (ln)
def natural_logarithm(x):
    if x <= 0:
        return "Error! Natural logarithm is not defined for zero or negative numbers."
    else:
        return math.log(x)

# Function to take user input and perform the desired operation
def calculator():
    print("Welcome to the Advanced Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation (x^y)")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Logarithm (base 10)")
    print("11. Sine")
    print("12. Cosine")
    print("13. Tangent")
    print("14. Power of 10 (10^x)")
    print("15. Natural Logarithm (ln)")
    
    while True:
        # Take input from the user for the operation
        choice = input("Enter choice (1-15): ")
        
        # Check if the choice is valid
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                # Take input from the user for two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            # Perform the selected operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = floor_division(num1, num2)
                print(f"{num1} // {num2} = {result}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '7':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
        
        elif choice in ['8', '9', '10', '11', '12', '13', '14', '15']:
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            # Perform single-number operations
            if choice == '8':
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '9':
                print(f"Factorial of {num} = {factorial(num)}")
            elif choice == '10':
                print(f"Logarithm (base 10) of {num} = {logarithm(num)}")
            elif choice == '11':
                print(f"Sine of {num} degrees = {sine(num)}")
            elif choice == '12':
                print(f"Cosine of {num} degrees = {cosine(num)}")
            elif choice == '13':
                print(f"Tangent of {num} degrees = {tangent(num)}")
            elif choice == '14':
                print(f"10^{num} = {power_of_ten(num)}")
            elif choice == '15':
                print(f"Natural logarithm of {num} = {natural_logarithm(num)}")
        
        else:
            print("Invalid input! Please select a valid operation (1-15).")
        
        # Ask the user if they want to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

# Call the calculator function
calculator()
