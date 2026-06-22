from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data = b"DoctorID001"

encrypted = cipher.encrypt(data)

decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted.decode())
print("Decrypted:", decrypted.decode())