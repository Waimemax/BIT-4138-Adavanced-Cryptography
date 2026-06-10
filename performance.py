import time
from Crypto.Cipher import ARC4

key = b"MedicalAuth123"

start = time.time()

for i in range(10000):
    cipher = ARC4.new(key)
    cipher.encrypt(b"STAFF_LOGIN")

end = time.time()

print("Encryption Performance Test")
print("Iterations:", 10000)
print("Execution Time:", round(end - start, 4), "seconds")