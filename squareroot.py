import math

def square_root(n):
    """Calculate the square root of a number."""
    if n < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(n)


number = float(input("Enter a number: "))
result = square_root(number)
print(f"Square root of {number} is {result}")