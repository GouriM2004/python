# Program to count word frequency in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word in freq:
    print(word, ":", freq[word])
