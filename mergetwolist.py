# Program to merge two lists and sort them

list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    list1.append(int(input(f"Enter element {i+1}: ")))

n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    list2.append(int(input(f"Enter element {i+1}: ")))

# Merge lists
merged_list = list1 + list2

# Sort merged list
for i in range(len(merged_list)):
    for j in range(i + 1, len(merged_list)):
        if merged_list[i] > merged_list[j]:
            merged_list[i], merged_list[j] = merged_list[j], merged_list[i]

print("Merged and Sorted List:", merged_list)
