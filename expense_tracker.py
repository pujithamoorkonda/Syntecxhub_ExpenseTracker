import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "transactions.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Date",
        "Type",
        "Category",
        "Amount"
    ])
    df.to_csv(FILE_NAME, index=False)


# Add Transaction
def add_transaction():

    date = input("Enter Date (YYYY-MM-DD): ")

    t_type = input("Income or Expense: ")

    category = input("Category: ")

    amount = float(input("Amount: "))

    data = {
        "Date": date,
        "Type": t_type,
        "Category": category,
        "Amount": amount
    }

    df = pd.read_csv(FILE_NAME)

    df = pd.concat([df, pd.DataFrame([data])],
                   ignore_index=True)

    df.to_csv(FILE_NAME, index=False)

    print("Transaction Added Successfully")


# View Transactions
def view_transactions():

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No transactions found")
    else:
        print(df)


# Monthly Summary
def monthly_summary():

    month = input("Enter Month (YYYY-MM): ")

    df = pd.read_csv(FILE_NAME)

    df['Date'] = pd.to_datetime(df['Date'])

    monthly = df[df['Date'].dt.strftime('%Y-%m') == month]

    income = monthly[monthly['Type'].str.lower() == 'income']['Amount'].sum()

    expense = monthly[monthly['Type'].str.lower() == 'expense']['Amount'].sum()

    balance = income - expense

    print("\n----- Monthly Summary -----")
    print(f"Income  : ₹{income}")
    print(f"Expense : ₹{expense}")
    print(f"Balance : ₹{balance}")


# Export Summary
def export_summary():

    month = input("Enter Month (YYYY-MM): ")

    df = pd.read_csv(FILE_NAME)

    df['Date'] = pd.to_datetime(df['Date'])

    monthly = df[df['Date'].dt.strftime('%Y-%m') == month]

    income = monthly[monthly['Type'].str.lower() == 'income']['Amount'].sum()

    expense = monthly[monthly['Type'].str.lower() == 'expense']['Amount'].sum()

    balance = income - expense

    summary = pd.DataFrame({
        "Month": [month],
        "Income": [income],
        "Expense": [expense],
        "Balance": [balance]
    })

    summary.to_csv("summary.csv", index=False)

    print("Summary Exported Successfully")


# Generate Chart
def generate_chart():

    df = pd.read_csv(FILE_NAME)

    expenses = df[df['Type'].str.lower() == 'expense']

    category_expense = expenses.groupby(
        'Category')['Amount'].sum()

    plt.figure(figsize=(8, 5))

    category_expense.plot(kind='bar')

    plt.title("Expenses by Category")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("expense_chart.png")

    plt.show()

    print("Chart Saved as expense_chart.png")


# Menu
while True:

    print("\n===== Expense Tracker =====")

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Monthly Summary")
    print("4. Export Summary")
    print("5. Generate Chart")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        export_summary()

    elif choice == "5":
        generate_chart()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")