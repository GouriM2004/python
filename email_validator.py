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

