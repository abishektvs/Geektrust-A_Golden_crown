def encrypt(message):
    cipher_key = len(message)
    encrypted_message = ""

    for letter in message:
        encrypted_ascii = ord(letter.upper()) + cipher_key

        if encrypted_ascii > 90:
            residue = encrypted_ascii - 90
            encrypted_ascii = 64 + residue

        encrypted_message += chr(encrypted_ascii)
    return encrypted_message

def count_letters(word):
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts
