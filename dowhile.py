# Python doesn't have a do-while loop, but we can simulate it
# This program will execute at least once, then continue while the condition is True

# Example 1: Simple counter with do-while pattern
print("=== Example 1: Counter ===")
count = 0
while True:
    print(f"Count is: {count}")
    count += 1
    if not (count < 5):  # Loop continues while count < 5
        break

# Example 2: User input with do-while pattern
print("\n=== Example 2: User Input ===")
while True:
    user_input = input("Enter a number (0 to exit): ")
    print(f"You entered: {user_input}")
    
    if user_input == "0":
        print("Exiting...")
        break

# Example 3: Menu system with do-while pattern
print("\n=== Example 3: Menu System ===")
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
