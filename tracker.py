import pandas as pd
from datetime import datetime

FILE = "data.csv"


def load_data():
    try:
        df = pd.read_csv(FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["category", "amount", "date"])
    return df


def save_data(df):
    df.to_csv(FILE, index=False)


def add_expense(category, amount):
    df = load_data()

    new_data = {
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    save_data(df)

    return "✅ Expense added successfully"

def view_expenses():
    df = load_data()

    if df.empty:
        return "No expenses found"

    return df

def total_spending():
    df = load_data()

    if df.empty:
        return "No expenses found"

    total = df["amount"].sum()
    avg = df["amount"].mean()
    count = len(df)

    return (
        f"\n💰 Total Spending: ₹{total}\n"
        f"📊 Average Expense: ₹{avg:.2f}\n"
        f"🧾 Total Entries: {count}"
    )

def category_summary():
    df = load_data()

    if df.empty:
        return "No expenses found"

    summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)

    result = "\n📊 Category-wise Spending (High → Low):\n"
    for category, amount in summary.items():
        result += f"{category}: ₹{amount}\n"

    return result

def filter_by_category(category):
    df = load_data()

    if df.empty:
        return "No expenses found"

    filtered = df[df["category"].str.lower() == category.lower()]

    if filtered.empty:
        return f"No expenses found for '{category}'"

    return filtered

def delete_expense(index):
    df = load_data()

    if df.empty:
        return "No expenses to delete"

    if index < 1 or index > len(df):
        return "Invalid expense number"

    removed = df.iloc[index - 1]

    df = df.drop(index=index - 1).reset_index(drop=True)

    save_data(df)

    return f"🗑️ Deleted: {removed['category']} - ₹{removed['amount']}"
