# Program to find frequency of each character in a string

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")
for key in freq:
    print(key, ":", freq[key])
