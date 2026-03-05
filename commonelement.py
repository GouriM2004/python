# Program to find common elements between two lists

list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    list1.append(int(input(f"Enter element {i+1}: ")))

n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    list2.append(int(input(f"Enter element {i+1}: ")))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)
