import time
import string

# Fake password (DO NOT use real passwords)
password = " mustafaisnoob "

characters = string.ascii_lowercase + string.digits
guessed = ""

print("🔐 PASSWORD CRACKER SIMULATOR 🔐")
print("Initializing brute force attack...\n")
time.sleep(1)

for real_char in password:
    for guess in characters:
        print(f"Trying: {guessed + guess}")
        time.sleep(0.05)

        if guess == real_char:
            guessed += guess
            print(f"✅ Character found: {guessed}\n")
            time.sleep(0.5)
            break

print("🚨 ACCESS GRANTED 🚨")
print("Password cracked:", guessed)
