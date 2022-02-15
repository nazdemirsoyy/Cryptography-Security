from collections import Counter

f = open("words.txt", "r")
article = f.read()

frequency = Counter(article)

frequency_stored = sorted(frequency, key = frequency.get, reverse=True)

for char in frequency_stored:
    if char.isalpha():
        print(char,frequency[char])
