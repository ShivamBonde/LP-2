#pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Function to pad the input text to be a multiple of 8 bytes (DES block size)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Encryption function
def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return encrypted_text

# Decryption function
def decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text).decode().strip()
    return decrypted_text

# Example usage
key = b'12345678'  # DES key should be 8 bytes long
plain_text = "Hello DES"

# Encrypt the text
encrypted = encrypt(plain_text, key)
print("Encrypted:", encrypted)

# Decrypt the text
decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
