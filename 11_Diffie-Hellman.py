# Given values for prime p and base g
p = 23  # A prime number
g = 5   # A primitive root modulo p

# Private keys for Alice and Bob
alice_private = 6
bob_private = 15

# Alice and Bob compute their public keys using pow function
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Alice and Bob compute the shared secret using the other's public key
alice_shared_secret = pow(bob_public, alice_private, p)
bob_shared_secret = pow(alice_public, bob_private, p)

# Print the shared secrets
print(f"Alice's Shared Secret: {alice_shared_secret}")
print(f"Bob's Shared Secret: {bob_shared_secret}")
