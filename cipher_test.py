def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

test_users = [
    "DOCTOR",
    "NURSE",
    "ADMIN",
    "TECHNICIAN",
    "PHARMACIST"
]

print("=== Cipher Testing Results ===\n")

for user in test_users:
    encrypted = caesar_encrypt(user, 3)
    print(f"Original: {user}")
    print(f"Encrypted: {encrypted}")
    print("-" * 30)