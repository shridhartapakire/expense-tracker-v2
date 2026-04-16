from tracker import add_expense, view_expenses, total_spending, category_summary, filter_by_category, delete_expense

def menu():
    print("\n===== EXPENSE TRACKER V2 💰 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Filter by Category")
    print("6. Delete Expense")
    print("7. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            print(add_expense(category, amount))
            print("-" * 40)

        elif choice == "2":
            data = view_expenses()
            print("\n📊 All Expenses:\n")
            for i, row in data.iterrows():
                print(f"{i+1}. {row['category']} - ₹{row['amount']} ({row['date']})")
            print("-" * 40)

        elif choice == "3":
            print(total_spending())
            print("-" * 40)

        elif choice == "4":
            print(category_summary())
            print("-" * 40)

        elif choice == "5":
            category = input("Enter category to filter: ")
            data = filter_by_category(category)

            if isinstance(data, str):
                 print(data)
            else:
                print(f"\n📂 Expenses for '{category}':\n")
                print(data.to_string(index=False))
            print("-" * 40)

        elif choice == "6":
            data = view_expenses()

            if isinstance(data, str):
                print(data)
            else:
                print("\n📋 All Expenses:\n")

                for i, row in data.iterrows():
                    print(f"{i+1}. {row['category']} - ₹{row['amount']} ({row['date']})")
                try:
                    index = int(input("Enter expense number to delete: "))
                    print(delete_expense(index))
                except ValueError:
                    print("Invalid input")
            print("-" * 40)

        elif choice == "7":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
