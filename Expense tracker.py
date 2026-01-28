import csv
from datetime import datetime

FILENAME = "expenses.csv"

# File exist nasel tar header create kara
def init_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!")


def show_summary():
    total = 0
    category_total = {}

    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row["Amount"])
            cat = row["Category"]

            total += amt
            category_total[cat] = category_total.get(cat, 0) + amt

    print("\n📊 Expense Summary")
    print("Total Expense: ₹", total)

    print("\nCategory-wise Expense:")
    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt}")

    if category_total:
        highest = max(category_total, key=category_total.get)
        print("\n🔥 Highest Spending Category:", highest)


def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            print("👋 Thank you! Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Main
init_file()
menu()