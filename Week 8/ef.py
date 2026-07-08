# Diffie-Hellman Key Exchange Implementation

print("===== Diffie-Hellman Key Exchange =====")

# Public values
p = int(input("Enter Public Prime (p): "))
g = int(input("Enter Generator (g): "))

# Private keys
alice_private = int(input("Enter Alice's Private Key: "))
bob_private = int(input("Enter Bob's Private Key: "))

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Compute shared secret
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

print("\n----- Results -----")
print("Alice Public Key :", alice_public)
print("Bob Public Key   :", bob_public)
print("Alice Secret     :", alice_secret)
print("Bob Secret       :", bob_secret)

if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
    print("Shared Secret =", alice_secret)
else:
    print("\nKey Exchange Failed.")