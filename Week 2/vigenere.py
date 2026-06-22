tests = ["NURSE", "DOCTOR", "ADMIN"]

for t in tests:
    encrypted = caesar_encrypt(t, 3)
    print(f"{t} -> {encrypted}")