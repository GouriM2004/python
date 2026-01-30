# Program to find square and cube using lambda function

square = lambda x: x * x
cube = lambda x: x * x * x

num = int(input("Enter a number: "))

print("Square of", num, "is", square(num))
print("Cube of", num, "is", cube(num))
