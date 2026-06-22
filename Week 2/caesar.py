def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

staff_id = "MED123"
encrypted = caesar_encrypt(staff_id, 3)

print("Original:", staff_id)
print("Encrypted:", encrypted)s