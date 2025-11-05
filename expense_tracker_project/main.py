# main.py

from modules.expense import Expense
from modules.file_operations import save_expense, load_expenses
from modules.category_summarizer import summarize_by_category

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    expense = Expense(amount, category, date)
    save_expense(expense)
    print("Expense added successfully!\n")

def main_menu():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            expenses = load_expenses()
            if not expenses:
                print("No expenses found.\n")
            else:
                print("\nAll Expenses:")
                for exp in expenses:
                    print(f"{exp.amount} / {exp.category} / {exp.date}")
                print()
        elif choice == "3":
            expenses = load_expenses()
            summarize_by_category(expenses)
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()