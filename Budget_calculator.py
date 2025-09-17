# Budget Calculator

income = float(input("Enter your monthly income: GHS "))
expenses = {}

while True:
    category = input("Enter expense category (or 'done' to finish): ")
    if category.lower() == 'done':
        break
    amount = float(input(f"Enter amount for {category}: GHS "))
    expenses[category] = amount

total_expense = sum(expense.value())

print("\n--- Budget Summary ---")
print(f"Total Income: GHS {income}")
print(f"Total Expenses: GHS {total_expenses}")
print(f"Remaining Balance: GHS {balance}")
