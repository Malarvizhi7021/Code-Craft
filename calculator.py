print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter choice (1-4): "))
a, b = float(input("Enter first number: ")), float(input("Enter second number: "))

if choice == 1:
    result = a + b
elif choice == 2:
    result = a - b
elif choice == 3:
    result = a * b
elif choice == 4:
    result = "Division by zero is not allowed" if b == 0 else a / b
else:
    result = "Invalid choice"

print("Result:", result)
