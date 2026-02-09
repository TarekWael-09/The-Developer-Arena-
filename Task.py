import csv
import shutil
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, filedialog

CSV_FILE = None
BACKUP_FILE = "backup_expenses.csv"


# ===================== DATA MODEL =====================
class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        return [self.amount, self.category, self.date, self.description]


# ===================== VALIDATION =====================
def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except:
        raise ValueError("Amount must be a positive number")


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except:
        raise ValueError("Date must be YYYY-MM-DD")


# ===================== CSV =====================
def choose_csv_file():
    global CSV_FILE
    CSV_FILE = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )

    if CSV_FILE:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date", "Description"])
        messagebox.showinfo("Saved", "CSV file created successfully")


def save_expense(expense):
    if not CSV_FILE:
        raise Exception("Please choose CSV file first")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())


def load_expenses():
    expenses = []
    if not CSV_FILE or not os.path.exists(CSV_FILE):
        return expenses

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(Expense(row[0], row[1], row[2], row[3]))
    return expenses


# ===================== REPORTS =====================
def total_expenses(expenses):
    return sum(e.amount for e in expenses)


def average_expense(expenses):
    return total_expenses(expenses) / len(expenses) if expenses else 0


def expenses_by_category(expenses):
    result = {}
    for e in expenses:
        result[e.category] = result.get(e.category, 0) + e.amount
    return result


# ===================== GUI ACTIONS =====================
def add_expense():
    try:
        amount = validate_amount(entry_amount.get())
        category = entry_category.get()
        date = validate_date(entry_date.get())
        description = entry_description.get()

        expense = Expense(amount, category, date, description)
        save_expense(expense)

        messagebox.showinfo("Success", "Expense added & saved to CSV")

        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_description.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_reports():
    expenses = load_expenses()

    report_text.delete("1.0", tk.END)
    report_text.insert(tk.END, f"Total Expenses: {total_expenses(expenses)}\n")
    report_text.insert(tk.END, f"Average Expense: {average_expense(expenses)}\n\n")
    report_text.insert(tk.END, "Expenses by Category:\n")

    for cat, total in expenses_by_category(expenses).items():
        report_text.insert(tk.END, f"- {cat}: {total}\n")


# ===================== GUI =====================
root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("420x550")

tk.Button(root, text="Choose CSV File", command=choose_csv_file, bg="lightblue").pack(pady=5)

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="Date (YYYY-MM-DD)").pack()
entry_date = tk.Entry(root)
entry_date.pack()

tk.Label(root, text="Description").pack()
entry_description = tk.Entry(root)
entry_description.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Reports", command=show_reports).pack(pady=5)

report_text = tk.Text(root, height=12)
report_text.pack(pady=10)

root.mainloop()
