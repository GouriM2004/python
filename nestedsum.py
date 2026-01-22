# Program to find the sum of a nested list

nested_list = []

n = int(input("Enter number of sublists: "))

for i in range(n):
    sublist = []
    m = int(input(f"Enter number of elements in sublist {i+1}: "))
    for j in range(m):
        sublist.append(int(input("Enter element: ")))
    nested_list.append(sublist)

total_sum = 0

for sub in nested_list:
    for item in sub:
        total_sum += item

print("Nested List:", nested_list)
print("Sum of nested list elements:", total_sum)
