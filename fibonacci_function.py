# Program to generate Fibonacci series using function

def fibonacci(n):
    a = 0
    b = 1

    if n <= 0:
        print("Enter a positive number")
    else:
        print("Fibonacci Series:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b


terms = int(input("Enter number of terms: "))
fibonacci(terms)
