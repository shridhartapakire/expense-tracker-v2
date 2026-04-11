from tracker import add_expense

category = input("Enter category: ")
amount = float(input("Enter amount: "))

print(add_expense(category, amount))