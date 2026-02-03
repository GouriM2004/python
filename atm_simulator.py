balance = 10000  # Initial balance

def show_menu():
    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount!")


    elif choice == "4":
        print("Thank you for using the ATM. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
