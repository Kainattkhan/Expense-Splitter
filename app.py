%%writefile app.py
import streamlit as st
import pandas as pd

st.title("Expense Splitter")

# Input for names of friends
friends = st.text_input("Enter names of friends (comma-separated):")
friends_list = [name.strip() for name in friends.split(",") if name.strip()]

# Input for expenses
expense_entries = []
if st.button("Add Expense"):
    expense_description = st.text_input("Expense Description")
    amount = st.number_input("Amount", min_value=0.0)
    selected_friends = st.multiselect("Select Friends", friends_list)

    if expense_description and selected_friends:
        expense_entries.append({
            "Description": expense_description,
            "Amount": amount,
            "Paid By": selected_friends
        })
        st.success("Expense added!")

# Show expenses
if expense_entries:
    st.write("### Expenses")
    expense_df = pd.DataFrame(expense_entries)
    st.dataframe(expense_df)

    # Calculate who owes what
    total_expenses = {}
    for entry in expense_entries:
        amount_per_person = entry["Amount"] / len(entry["Paid By"])
        for friend in friends_list:
            if friend not in total_expenses:
                total_expenses[friend] = 0
        for payer in entry["Paid By"]:
            total_expenses[payer] += amount_per_person

    st.write("### Summary Report")
    for friend, total in total_expenses.items():
        st.write(f"{friend} owes: ${total:.2f}")
