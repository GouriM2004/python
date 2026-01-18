# Program to convert string to title case manually

text = input("Enter a string: ")

result = ""
capitalize = True

for ch in text:
    if ch == " ":
        result += ch
        capitalize = True
    else:
        if capitalize:
            result += ch.upper()
            capitalize = False
        else:
            result += ch.lower()

print("Title Case String:", result)
