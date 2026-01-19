# Program to remove duplicate elements from a list

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
