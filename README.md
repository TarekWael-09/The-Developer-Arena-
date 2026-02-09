PersonalFinanceManager/
│
├─ README.md
├─ main.py
├─ requirements.txt
│
├─ src/
│   └─ expense_manager.py  # ممكن تحط الكود اللي انت عاملته هنا
│
├─ data/
│   └─ sample_expenses.csv  # ممكن تحط بيانات تجريبية هنا
│
├─ docs/
│   └─ user_guide.md
│
├─ tests/
│   └─ test_expense_manager.py
│
PersonalFinanceManager/
└─ screenshots/
   └─ app_screenshot.png  <-- الصورة اللي انت رفعته

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
pip install -r requirements.txt
python main.py

---

### **2️⃣ main.py**
```python
from src.expense_manager import *

if __name__ == "__main__":
    start_app()
