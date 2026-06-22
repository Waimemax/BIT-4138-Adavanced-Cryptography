from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("Generated AES Key:")
print(key.decode())