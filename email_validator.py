import re
import tkinter as tk

def validate_email():
    email = entry.get()

    # Email regex pattern
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        result_label.config(text="Valid Email ✅", fg="green")
    else:
        result_label.config(text="Invalid Email ❌", fg="red")

# -------- UI --------
window = tk.Tk()
window.title("Email Validator")
window.geometry("400x200")
window.resizable(False, False)

tk.Label(window, text="Enter Email Address", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, width=35)
entry.pack(pady=5)

tk.Button(window, text="Validate Email", command=validate_email).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

window.mainloop()
