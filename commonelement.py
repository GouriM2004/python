
common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)
