categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']
expenses = []

def add_expense():
    category = input(f"Enter Category among {categories}: ")
    if category not in categories:
        print("Invalid category. Adding to 'Other'.")
        category = 'Other'
    
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return  # The return statement exits the function early,
                    # before the rest of the code continue running with invalid amount

    
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        'category' : category,
        'amount' : amount,
        'date' : date
    }
    expenses.append(expense)
    print("✅ Expense added!\n")

def view_expenses():
    if expenses == None:
        print("No expenses yet!")

    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} | {exp['amount']} | {exp['date']}")

def total_spent():
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💰 Total spent: {total} Toman\n")

add_expense()
view_expenses()
total_spent()