# modules/category_summarizer.py

def summarize_by_category(expenses):
    summary = {}
    for exp in expenses:
        summary[exp.category] = summary.get(exp.category, 0) + exp.amount

    if not summary:
        print("No expenses to summarize.")
        return

    print("\n--- Expense Summary by Category ---")
    print(f"{'Category':<15}{'Total Amount'}")
    print("==================================")
    for category, total in summary.items():
        print(f"{category:<15}{total:.2f}")
    print("==================================\n")