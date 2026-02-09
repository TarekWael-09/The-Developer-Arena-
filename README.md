# Personal Finance Manager

A simple desktop application to manage personal expenses, save them to CSV, and view reports.

## Features
- Add expenses with amount, category, date, and description.
- Save expenses to CSV file.
- View reports: total expenses, average expense, and breakdown by category.
- Simple GUI using Tkinter.

## Setup

1. Clone this repository:
```bash
git clone <repo_url>
cd PersonalFinanceManager
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python main.py
PersonalFinanceManager/
│
├─ README.md
├─ main.py
├─ requirements.txt
│
├─ src/
│   └─ expense_manager.py  # Contains the main logic for managing expenses
│
├─ data/
│   └─ sample_expenses.csv  # Sample CSV file with expenses
│
├─ docs/
│   └─ user_guide.md        # User guide documentation
│
├─ tests/
│   └─ test_expense_manager.py  # Unit tests for expense manager
│
└─ screenshots/
    └─ app_screenshot.png      # Screenshot of the app
