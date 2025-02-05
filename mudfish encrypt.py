import random
import math

# Encoding dictionary for A-Z -> 1-26, space -> 28
encoding = {chr(i): i - 64 for i in range(65, 91)}
encoding[' '] = 28  # space -> 28

decoding = {v: k for k, v in encoding.items()}

def encrypt_message(message, e, n):
    message = message.upper()
    message_encoded = [encoding[ch] for ch in message]
    ciphertext = [pow(ch, e, n) for ch in message_encoded]
    return ciphertext

def decrypt_message(ciphertext, d, n):
    message_encoded_decrypted = [pow(ch, d, n) for ch in ciphertext]
    message_decrypted = "".join(decoding[ch] for ch in message_encoded_decrypted)  #
    return message_decrypted
n = 1271
e = 17

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

def factorize_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

p, q = factorize_n(n)
phi_n = (p - 1) * (q - 1)
d = mod_inverse(e, phi_n)

message = "The lecture is interactive and you need to improve on your teaching techniques and the lecture is seven out ten"

ciphertext = encrypt_message(message, e, n)
print("Ciphertext:", ciphertext)

message_decrypted = decrypt_message(ciphertext, d, n)
print("Decrypted message:", message_decrypted)