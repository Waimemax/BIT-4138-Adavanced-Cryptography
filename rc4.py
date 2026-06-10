from Crypto.Cipher import ARC4

key = b"MedicalAuth123"
plaintext = b"STAFF_LOGIN"

cipher = ARC4.new(key)

ciphertext = cipher.encrypt(plaintext)

print("Plaintext :", plaintext.decode())
print("Encrypted :", ciphertext.hex())