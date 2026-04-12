from tracker import add_expense, view_expenses


def menu():
    print("\n===== EXPENSE TRACKER V2 💰 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            print(add_expense(category, amount))

        elif choice == "2":
            data = view_expenses()
            print("\n📊 All Expenses:\n")
            print(data.to_string(index=False))

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
