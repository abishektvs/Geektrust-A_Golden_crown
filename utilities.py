
def encrypt_emblem(emblem):
    cipher_key = len(emblem)
    encrypted_emblem = ""

    for letter in emblem:
        encrypted_ascii = ord(letter.upper()) + cipher_key

        if encrypted_ascii > 90:
            residue = encrypted_ascii - 90
            encrypted_ascii = 65 + residue - 1

        encrypted_emblem += chr(encrypted_ascii)
    return list(encrypted_emblem)

def count_letters(word):
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    return counts
