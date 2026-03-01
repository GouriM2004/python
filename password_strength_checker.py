import re
import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        result = "Weak Password ❌"
        color = "red"
    elif score <= 4:
        result = "Medium Password ⚠️"
        color = "orange"
    else:
        result = "Strong Password ✅"
        color = "green"

    result_label.config(text=result, fg=color)

# -------- UI --------
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x250")
window.resizable(False, False)

tk.Label(window, text="Enter Password", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, width=30, show="*")
entry.pack(pady=5)

tk.Button(window, text="Check Strength", command=check_strength).pack(pady=15)


