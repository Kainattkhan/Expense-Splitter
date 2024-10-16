import streamlit as st
import pandas as pd

# Streamlit title
st.title("Expense Splitter")

# Step 1: Input names of friends (comma-separated)
friends = st.text_input("Enter names of friends (comma-separated):")
if friends:
    friends_list = [name.strip() for name in friends.split(",")]

    # Step 2: Initialize a list to store expenses in session state
    if 'expense_entries' not in st.session_state:
        st.session_state['expense_entries'] = []

    # Step 3: Adding expenses
    with st.form(key='expense_form'):
        expense_description = st.text_input("Expense Description")
        amount = st.number_input("Amount", min_value=0.0)
        paid_by = st.multiselect("Who paid for this?", friends_list)

        submit_button = st.form_submit_button(label='Add Expense')
        
        if submit_button:
            if expense_description and paid_by:
                st.session_state['expense_entries'].append({
                    "Description": expense_description,
                    "Amount": amount,
                    "Paid By": paid_by
                })
                st.success(f"Expense '{expense_description}' added!")
            else:
                st.error("Please provide a description and select friends who paid.")

    # Step 4: Display all expenses
    if st.session_state['expense_entries']:
        expense_df = pd.DataFrame(st.session_state['expense_entries'])
        st.write("### List of Expenses")
        st.dataframe(expense_df)

        # Step 5: Calculate how much each person owes
        total_expenses = {friend: 0 for friend in friends_list}

        for entry in st.session_state['expense_entries']:
            amount_per_person = entry["Amount"] / len(entry["Paid By"])
            for payer in entry["Paid By"]:
                total_expenses[payer] += amount_per_person

        # Step 6: Display the summary report
        st.write("### Summary Report")
        for friend, total in total_expenses.items():
            st.write(f"{friend} owes: ${total:.2f}")
