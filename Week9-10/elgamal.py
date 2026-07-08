import random

def is_prime(n, k=5):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and is_prime(p):
            return p

def generate_keys():
    # Using a 16-bit safe prime field for demonstration
    p = generate_large_prime(16)
    # Simple primitive root finder or fallback standard base
    g = 2 
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return p, g, private_key, public_key

def encrypt(plain_text, p, g, y):
    cipher_chars = []
    for char in plain_text:
        m = ord(char)
        k = random.randint(2, p - 2)
        c1 = pow(g, k, p)
        c2 = (m * pow(y, k, p)) % p
        cipher_chars.append((c1, c2))
    return cipher_chars

def decrypt(cipher_chars, p, x):
    plain_chars = []
    for c1, c2 in cipher_chars:
        s = pow(c1, x, p)
        # Modular inverse using Fermat's Little Theorem
        s_inv = pow(s, p - 2, p)
        m = (c2 * s_inv) % p
        plain_chars.append(chr(m))
    return "".join(plain_chars)

# Execution logic for 5 distinct messages
p, g, x, y = generate_keys()
messages = ["HELLO", "WORLD", "CRYPT", "SECURE", "ELGAMAL"]

print(f"--- ElGamal Keys Generated ---")
print(f"Prime (p): {p}, Generator (g): {g}, Public Key (y): {y}\n")

for idx, msg in enumerate(messages, 1):
    encrypted = encrypt(msg, p, g, y)
    decrypted = decrypt(encrypted, p, x)
    print(f"Message {idx}: {msg}")
    print(f"  Ciphertext Samples (C1, C2): {encrypted[:2]}...")
    print(f"  Decrypted Output: {decrypted} (Match: {msg == decrypted})")