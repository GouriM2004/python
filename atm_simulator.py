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



    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
