# This program collects monthly expenses from the user, validates inputs, and uses the reduce method
# to calculate the total, highest, and lowest expenses, displaying their types.

from functools import reduce

# Collect expenses from the user with validation
def collect_expenses():
    # Initialize list to store expenses
    expenses = []
    
    print("Enter your monthly expenses (type 'done' for expense type to finish):")
    
    # Loop to collect expenses
    while True:
        # Get expense type
        expense_type = input("Enter expense type (or 'done' to finish): ").strip()
        if expense_type.lower() == 'done':
            if not expenses:
                print("No expenses entered. Please enter at least one expense.")
                continue
            break
        
        # Get expense amount with validation
        try:
            amount = float(input(f"Enter amount for {expense_type} ($): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            expenses.append({"type": expense_type, "amount": amount})
        except ValueError:
            print("Please enter a valid number for the amount.")
    
    return expenses

# Analyze expenses using reduce to calculate total, highest, and lowest
def analyze_expenses(expenses):
    # Calculate total using reduce
    total = reduce(lambda acc, exp: acc + exp["amount"], expenses, 0.0)
    
    # Find highest expense using reduce
    highest = reduce(
        lambda acc, exp: exp if exp["amount"] > acc["amount"] else acc,
        expenses,
        {"type": "None", "amount": float('-inf')}
    )
    
    # Find lowest expense using reduce
    lowest = reduce(
        lambda acc, exp: exp if exp["amount"] < acc["amount"] else acc,
        expenses,
        {"type": "None", "amount": float('inf')}
    )
    
    return total, highest, lowest

# Main function to orchestrate expense collection and analysis
def main():
    # Collect expenses
    expenses = collect_expenses()
    
    # Analyze expenses
    total, highest, lowest = analyze_expenses(expenses)
    
    # Display results
    print("\n--- Expense Analysis Results ---")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} (${highest['amount']:.2f})")
    print(f"Lowest Expense: {lowest['type']} (${lowest['amount']:.2f})")

# Entry point of the program
if __name__ == "__main__":
    main()