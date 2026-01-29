# Program to find union, intersection and difference of sets

set1 = set()
set2 = set()

n1 = int(input("Enter number of elements in first set: "))
for i in range(n1):
    set1.add(int(input(f"Enter element {i+1}: ")))

n2 = int(input("Enter number of elements in second set: "))
for i in range(n2):
    set2.add(int(input(f"Enter element {i+1}: ")))

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)
