# Encryption function
def encrypt(plaintext, key):
    # Create an empty list to store the ciphertext
    ciphertext = [''] * key

    # Loop over the plaintext and place each character in the correct column
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key

    return ''.join(ciphertext)

# Decryption function
def decrypt(ciphertext, key):
    # Number of rows and columns
    num_rows = len(ciphertext) // key
    num_cols = key
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)

    # Create a list to store the decrypted text
    plaintext = [''] * num_rows

    # Loop over the ciphertext and place each character in the correct position
    col, row = 0, 0
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if row == num_rows or (row == num_rows - 1 and col >= num_cols - num_shaded_boxes):
            row = 0
            col += 1

    return ''.join(plaintext)

# Example usage
plaintext = "HELLO"
key = 3

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
