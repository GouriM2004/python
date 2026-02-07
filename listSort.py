numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)
