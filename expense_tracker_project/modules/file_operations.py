# file_operations.py

import os
from modules.expense import Expense   

DATA_FILE = "data/expenses.txt"

def save_expense(expense):
    #Save a single expense object to the data file.
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "a") as file:
        file.write(expense.to_string() + "\n")


def load_expenses():
    #Load all expenses from the data file.
    expenses = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    expenses.append(Expense.from_string(line))
    return expenses