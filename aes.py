import time
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

start = time.time()

for i in range(1000):
    cipher.encrypt(b"DoctorID001")

end = time.time()

print("AES Performance Test")
print("Execution Time:", round(end - start,4),"seconds")