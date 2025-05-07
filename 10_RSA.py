# Predefined primes for simplicity
p, q = 61, 53
n = p * q
phi_n = (p - 1) * (q - 1)

# Public key exponent (e) and private key exponent (d)
e, d = 17, 2753

# Public and private keys
public_key = (e, n)
private_key = (d, n)

# RSA Encryption
def encrypt(text, key):
    e, n = key
    return [pow(ord(c), e, n) for c in text]

# RSA Decryption
def decrypt(cipher, key):
    d, n = key
    return ''.join([chr(pow(c, d, n)) for c in cipher])

# Example usage
text = "HELLO"
cipher = encrypt(text, public_key)
decrypted = decrypt(cipher, private_key)

print("Encrypted:", cipher)
print("Decrypted:", decrypted)
