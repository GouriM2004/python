
character = input("Enter a character: ")

if len(character) == 1:
    ascii_value = ord(character)
    print(f"ASCII value of '{character}' is {ascii_value}")
else:
    print("Please enter only one character")