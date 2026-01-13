# Array operations in Python using lists

# Create an array
arr = [10, 20, 30, 40, 50]

# Display array
print("Array:", arr)

# Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Add element
arr.append(60)
print("After append:", arr)

# Insert element at index
arr.insert(2, 25)
print("After insert:", arr)

# Remove element
arr.remove(25)
print("After remove:", arr)

# Array length
print("Length:", len(arr))

# Iterate through array
print("Elements:")
for element in arr:
    print(element)

# Array slicing
print("Slice [1:4]:", arr[1:4])

# Sort array
arr_copy = arr.copy()
arr_copy.sort()
print("Sorted:", arr_copy)