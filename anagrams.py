# Program to check whether two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
s1 = str1.replace(" ", "").lower()
s2 = str2.replace(" ", "").lower()

if len(s1) != len(s2):
    print("The strings are NOT anagrams")
else:
    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    if freq1 == freq2:
        print("The strings are anagrams")
    else:
        print("The strings are NOT anagrams")
