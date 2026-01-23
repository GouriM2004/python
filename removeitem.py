# Program to remove items from a set based on a condition

my_set = set()

n = int(input("Enter number of elements in set: "))
for i in range(n):
    my_set.add(int(input(f"Enter element {i+1}: ")))

limit = int(input("Remove elements less than: "))

remove_items = set()

for item in my_set:
    if item < limit:
        remove_items.add(item)

for item in remove_items:
    my_set.remove(item)

print("Updated set:", my_set)
