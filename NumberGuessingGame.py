import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess the number between 1 and 100")

while True:
   
        if guess < secret_number:
            print("Too Low ⬇️")
        elif guess > secret_number:
            print("Too High ⬆️")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number!")
