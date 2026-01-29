# Program to check subset and superset

set1 = set()
set2 = set()

n1 = int(input("Enter number of elements in first set: "))
for i in range(n1):
    set1.add(int(input(f"Enter element {i+1}: ")))

n2 = int(input("Enter number of elements in second set: "))
for i in range(n2):
    set2.add(int(input(f"Enter element {i+1}: ")))

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is NOT a subset of Set2")

if set1.issuperset(set2):
    print("Set1 is a superset of Set2")
else:
    print("Set1 is NOT a superset of Set2")
