print("1. Square")
print("2. Cube")

choice = int(input("Enter choice: "))
n = int(input("Enter number: "))

if choice == 1:
    print("Square =", n*n)
elif choice == 2:
    print("Cube =", n*n*n)
else:
    print("Invalid choice")
