def compare_numbers(num1, num2):
    comparison_dict = {
        '>': num1 > num2,
        '>=': num1 >= num2,
        '<': num1 < num2,
        '<=': num1 <= num2,
        '==': num1 == num2,
        '!=': num1 != num2
    }
    
    for operator, result in comparison_dict.items():
        print(f"{num1} {operator} {num2}: {result}")
