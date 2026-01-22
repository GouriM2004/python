# Program to split a list into even and odd lists

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even list:", even_list)
print("Odd list:", odd_list)
