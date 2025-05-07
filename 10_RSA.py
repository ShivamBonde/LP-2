# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

# Function to find modular inverse
def mod_inverse(e, phi_n):
    g, x, y = extended_gcd(e, phi_n)
    if g != 1:
        raise ValueError("Error: Modular inverse does not exist")
    else:
        return x % phi_n

# Predefined primes for simplicity
p, q = 61, 53
n = p * q
phi_n = (p - 1) * (q - 1)

# Public key exponent (e) and private key exponent (d)
e = 17
d = mod_inverse(e, phi_n)

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
