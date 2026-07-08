import random
import hashlib
import sys

def miller_rabin(n, k=5):
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
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else:
            return False
    return True

def get_prime(bits=16):
    while True:
        n = random.getrandbits(bits)
        if n % 2 != 0 and miller_rabin(n):
            return n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0: x1 += m0
    return x1

# Global state for key persistence across options
keys = {}

def menu():
    while True:
        print("\n=================================")
        print(" RSA SECURITY SYSTEM")
        print("=================================")
        print("1. Generate RSA Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Sign Message")
        print("5. Verify Signature")
        print("6. Miller-Rabin Prime Test")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        if choice == '1':
            p = get_prime(16)
            q = get_prime(16)
            while p == q:
                q = get_prime(16)
            n = p * q
            phi = (p - 1) * (q - 1)
            
            e = 65537
            while gcd(e, phi) != 1:
                e = random.randint(2, phi - 1)
                
            d = mod_inverse(e, phi)
            keys.update({'p': p, 'q': q, 'n': n, 'phi': phi, 'e': e, 'd': d})
            
            print(f"\n[+] Keys Generated Successfully!")
            print(f"Prime P: {p}\nPrime Q: {q}\nModulus n: {n}\nEuler Totient: {phi}\nPublic Key (e): {e}\nPrivate Key (d): {d}")
            
        elif choice == '2':
            if 'e' not in keys:
                print("[-] Please generate keys first!"); continue
            msg = input("Enter plaintext message: ")
            print(f"\nOriginal\tASCII\tEncrypted")
            cipher = []
            for char in msg:
                ascii_val = ord(char)
                enc_val = pow(ascii_val, keys['e'], keys['n'])
                cipher.append(enc_val)
                print(f"{char}\t\t{ascii_val}\t{enc_val}")
            keys['last_cipher'] = cipher
            
        elif choice == '3':
            if 'd' not in keys or 'last_cipher' not in keys:
                print("[-] No keys or ciphertext available to decrypt!"); continue
            print(f"\nEncrypted\t->\tDecrypted ASCII\t->\tOriginal Message")
            decrypted_chars = []
            for item in keys['last_cipher']:
                dec_ascii = pow(item, keys['d'], keys['n'])
                char = chr(dec_ascii)
                decrypted_chars.append(char)
                print(f"{item}\t\t{dec_ascii}\t\t\t{char}")
            print(f"\nFull Decrypted Message: {''.join(decrypted_chars)}")
            
        elif choice == '4':
            if 'd' not in keys:
                print("[-] Please generate keys first!"); continue
            msg = input("Enter message to sign: ")
            msg_hash = hashlib.sha256(msg.encode()).hexdigest()
            hash_int = int(msg_hash, 16) % keys['n']
            signature = pow(hash_int, keys['d'], keys['n'])
            keys['last_sig'] = (msg_hash, signature)
            print(f"\nOriginal Hash: {msg_hash}")
            print(f"Digital Signature: {signature}")
            
        elif choice == '5':
            if 'last_sig' not in keys:
                print("[-] No signature recorded to verify!"); continue
            orig_hash, signature = keys['last_sig']
            recovered_hash_int = pow(signature, keys['e'], keys['n'])
            current_msg = input("Enter message to verify against signature: ")
            current_hash = hashlib.sha256(current_msg.encode()).hexdigest()
            current_hash_int = int(current_hash, 16) % keys['n']
            
            if recovered_hash_int == current_hash_int:
                print("\n[+] Signature Valid")
            else:
                print("\n[-] Signature Invalid")
                
        elif choice == '6':
            print("\nGenerating 10 random numbers and testing:")
            print(f"Number\t\t|\tResult")
            print("-" * 35)
            for _ in range(10):
                num = random.randint(10, 1000)
                res = "Prime" if miller_rabin(num) else "Composite"
                print(f"{num}\t\t|\t{res}")
                
        elif choice == '7':
            print("Exiting system...")
            sys.exit(0)

if __name__ == "__main__":
    menu()