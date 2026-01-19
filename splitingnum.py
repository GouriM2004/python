# Program to split a list into even and odd lists

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)
