# modules/expense.py

class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = date

    def to_string(self):
        return f"{self.amount},{self.category},{self.date}"

    @staticmethod
    def from_string(data_str):
        amount, category, date = data_str.strip().split(',')
        return Expense(amount, category, date)