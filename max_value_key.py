# Program to find key with maximum value in dictionary

data = {}

n = int(input("Enter number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

max_key = None
max_value = -10**9

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)