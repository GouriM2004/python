# Program to sort dictionary by values

data = {}

n = int(input("Enter number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))

print("Dictionary sorted by values:", sorted_dict)
