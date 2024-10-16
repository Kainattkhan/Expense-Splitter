# Expense Splitter

A simple web-based application built with **Streamlit** to help groups split bills among friends, track who owes whom, and generate a summary report. This app is ideal for managing expenses during group outings, shared living situations, or travel.

## Features
- **Add Friends**: Input the names of friends who are part of the shared expenses.
- **Add Expenses**: Easily record expenses with a description, amount, and who paid for it.
- **Expense Tracking**: View a detailed list of all added expenses.
- **Summary Report**: Automatically calculate and display how much each friend owes based on the shared expenses.

## How It Works
1. Enter the names of friends (comma-separated).
2. Add expenses, specifying the description, the amount, and who paid.
3. The app calculates and shows how much each person owes based on their contributions.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kainattkhan/Expense-Splitter.git
   cd Expense-Splitter
   ```

2. **Install the required dependencies:**
   Ensure that you have Python installed, then use pip to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501` to interact with the app.

## How to Use

- Enter the names of friends in the text box.
- Add expenses one by one by providing a description, amount, and selecting who paid for it.
- A summary report is automatically generated showing how much each friend owes.

## Demo

You can try the live app https://expense-splitter-xwg7pt49tq79mubrqwclhy.streamlit.app/

## Built With
- **Streamlit** - Web framework for interactive data apps.
- **Pandas** - Used for data manipulation and analysis.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are always welcome!
