# Method 1: Using a temporary variable
a = 10
b = 20

print(f"Before swap: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After swap: a = {a}, b = {b}")