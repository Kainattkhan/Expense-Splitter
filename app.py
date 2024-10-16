import pandas as pd

# Step 1: Input names of friends (comma-separated)
friends = input("Enter names of friends (comma-separated): ")
friends_list = [name.strip() for name in friends.split(",")]

# Step 2: Initialize a list to store expenses
expense_entries = []

# Step 3: Adding expenses
while True:
    expense_description = input("Enter expense description (or type 'done' to finish): ")
    if expense_description.lower() == 'done':
        break

    amount = float(input("Enter amount: "))
    
    print("Friends List:", friends_list)
    paid_by = input("Who paid for this? (comma-separated names from the list): ")
    paid_by_list = [name.strip() for name in paid_by.split(",")]

    expense_entries.append({
        "Description": expense_description,
        "Amount": amount,
        "Paid By": paid_by_list
    })

# Step 4: Display all expenses
expense_df = pd.DataFrame(expense_entries)
print("\nList of Expenses:")
print(expense_df)

# Step 5: Calculate how much each person owes
total_expenses = {friend: 0 for friend in friends_list}

for entry in expense_entries:
    amount_per_person = entry["Amount"] / len(entry["Paid By"])
    for payer in entry["Paid By"]:
        total_expenses[payer] += amount_per_person

# Step 6: Display the summary report
print("\nSummary Report:")
for friend, total in total_expenses.items():
    print(f"{friend} owes: ${total:.2f}")

