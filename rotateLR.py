# Program to rotate a list left or right by N positions

numbers = []

n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

k = int(input("Enter number of positions to rotate: "))
direction = input("Enter direction (L for Left / R for Right): ").upper()

k = k % n   # to handle rotation greater than list size

if direction == 'L':
    for _ in range(k):
        first = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[-1] = first

elif direction == 'R':
    for _ in range(k):
        last = numbers[-1]
        for i in range(len(numbers) - 1, 0, -1):
            numbers[i] = numbers[i - 1]
        numbers[0] = last

else:
    print("Invalid direction")

print("Rotated List:", numbers)
