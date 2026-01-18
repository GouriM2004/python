# Program to find the second largest element in a list

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

largest = second_largest = -10**9  # very small number

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element is:", second_largest)
