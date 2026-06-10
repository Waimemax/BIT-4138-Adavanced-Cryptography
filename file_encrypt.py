from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

with open("staff.txt", "wb") as file:
    file.write(b"Medical Equipment Administrator")

with open("staff.txt", "rb") as file:
    data = file.read()

encrypted = cipher.encrypt(data)

with open("staff.enc", "wb") as file:
    file.write(encrypted)

print("File encrypted successfully.")