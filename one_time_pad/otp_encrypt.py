from brute_force import LETTERS


def encrypt(plain,key):
    cipher=""

    for i in range (len(plain)):
        char = plain[i]
        k = LETTERS.find(key[i])

        if (char.isupper()):
            cipher += chr((ord(char) + k - 65 ) % 26 + 65)
        else:
            cipher += chr((ord(char) + k - 97 ) % 26 + 97)
    return cipher
