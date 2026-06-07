from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

message = b"Human Matrix Medical Equipment"

encrypted = cipher.encrypt(message)

decrypted = cipher.decrypt(encrypted)

print("Original:", message.decode())
print("Encrypted:", encrypted.decode())
print("Decrypted:", decrypted.decode())
