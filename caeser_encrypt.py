import string

text = input("Please input your text: ")
key = int(input("Input your shift: "))

result =""

for i in range(len(text)):
    char = text[i]

    if (char.isupper()):
        result+= chr((ord(char) + key -65)%26 +65)
    else:
        result+= chr((ord(char) + key -975)%26 +97)

print("Key: " + str(key))
print("Original: " + text)
print("Encrypted: " + result)
