decrypted_message = "Dwkdu Pxedudn"
shift_key = 3
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)
encrypted_message = ""
for char in decrypted_message:
    if char.isalpha():
        is_upper = char.isupper()
        is_lower = char.lower()

        current_index = ALPHABET.index(is_lower)
        encrypted_index = (current_index - shift_key) % ALPHABET_SIZE
        encrypted_char = ALPHABET[encrypted_index]

        if is_upper:
            encrypted_message += encrypted_char.upper()
        else:
            encrypted_message += encrypted_char
    else:
        encrypted_message += char

print("Decrypted Message:", decrypted_message)
print("Encrypted Message:", encrypted_message)
