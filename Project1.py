import json
from datetime import datetime

expenses = []
budgets = {}

def add_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Transport, Utilities): ")
    amount = float(input("Enter amount: "))
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })
    print("Expense added successfully.\n")

def set_budget():
    category = input("Enter category to set budget for: ")
    amount = float(input("Enter monthly budget amount: "))
    budgets[category] = amount
    print(f"Budget set for {category}: ${amount}\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ${exp['amount']:.2f}")
    print()

def view_summary():
    print("\n--- Monthly Summary ---")
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
    
    for category, total in category_totals.items():
        budget = budgets.get(category)
        if budget:
            print(f"{category}: Spent ${total:.2f} / Budget ${budget:.2f}")
        else:
            print(f"{category}: Spent ${total:.2f} (No budget set)")
    print()

def save_to_file(filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump({"expenses": expenses, "budgets": budgets}, f)
    print("Data saved successfully.\n")

def load_from_file(filename="expenses.json"):
    global expenses, budgets
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            expenses = data.get("expenses", [])
            budgets = data.get("budgets", {})
            print("Data loaded successfully.\n")
    except FileNotFoundError:
        print("No saved data found.\n")

def run():
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. View Summary")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Select an option (1-7): ")
        print()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    run()