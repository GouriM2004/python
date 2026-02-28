import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

