# Personal Finance Manager

**Personal Finance Manager** is a simple Python application to track personal expenses, save them to CSV, and manage finances efficiently.  
It allows adding expenses, backing up data, and viewing sample reports.  

---

## Features
- Add expenses with:
  - Amount
  - Category
  - Date (optional, defaults to today)
  - Description
- Save expenses to a CSV file.
- Backup your expense data easily.
- CLI interface (can be extended to GUI in future versions).
- Easy to extend with reports and charts.

---

## Project Structure

PersonalFinanceManager/
│
├─ README.md
├─ main.py
├─ requirements.txt
│
├─ src/
│ └─ expense_manager.py # Main logic for managing expenses
│
├─ data/
│ └─ sample_expenses.csv # Sample CSV with expenses
│
├─ docs/
│ └─ user_guide.md # User guide
│
├─ tests/
│ └─ test_expense_manager.py # Unit tests
│
└─ screenshots/
└─ app_screenshot.png # Screenshot of the app

---

## Setup

1. Clone the repository:

```bash
git clone <repo_url>
cd PersonalFinanceManager
pip install -r requirements.txt
python src/expense_manager.py
