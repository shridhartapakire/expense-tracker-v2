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
    return f"💰 Total Spending: ₹{total}"

def category_summary():
    df = load_data()

    if df.empty:
        return "No expenses found"

    summary = df.groupby("category")["amount"].sum()

    result = "\n📊 Category-wise Spending:\n"
    for category, amount in summary.items():
        result += f"{category}: ₹{amount}\n"

    return result