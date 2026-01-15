# Program to reverse a string without using built-in functions

text = input("Enter a string: ")
reversed_str = ""

for char in text:
    reversed_str = char + reversed_str

print("Reversed string:", reversed_str)
