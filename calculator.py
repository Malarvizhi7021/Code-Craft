def calculator():
    #Asking for user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    #Performing calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif operator == '%':
        result = num1 % num2
    else:
        print("Error: Invalid operator.")
        return
    #Displaying the result
    print(f"Result: {result}")
#Call the calculator function
calculator()
