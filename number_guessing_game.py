import tkinter as tk
import random

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < secret_number:
            result_label.config(text="Too Low ⬇️", fg="orange")
        elif guess > secret_number:
            result_label.config(text="Too High ⬆️", fg="orange")
        else:
            result_label.config(
                text=f"Correct! 🎉 Attempts: {attempts}",
                fg="green"
            )
            guess_button.config(state="disabled")

    except ValueError:
        result_label.config(text="Please enter a valid number", fg="red")

# -------- UI --------
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("420x260")
window.resizable(False, False)

tk.Label(window, text="Guess a number (1–100)", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, width=25)
entry.pack(pady=5)


