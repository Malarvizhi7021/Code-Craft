def arrays_equal(a, b):
    if len(a) != len(b):  # If lengths differ, they can't be equal
        return False
    
    return sorted(a) == sorted(b)  # Sort both arrays and compare

# Example usage
a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]  
print(arrays_equal(a, b))  # Output: True
