# Program to count vowels and consonants in a string

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():   # check only alphabets
        if ch in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
