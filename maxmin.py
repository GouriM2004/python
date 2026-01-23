# Program to find maximum and minimum element in a tuple

my_tuple = ()

n = int(input("Enter number of elements in tuple: "))

temp_list = []
for i in range(n):
    temp_list.append(int(input(f"Enter element {i+1}: ")))

my_tuple = tuple(temp_list)

maximum = my_tuple[0]
minimum = my_tuple[0]

for item in my_tuple:
    if item > maximum:
        maximum = item
    if item < minimum:
        minimum = item

print("Tuple:", my_tuple)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
