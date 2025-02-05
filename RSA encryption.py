import rsa

def encode_message(message):

    encoding_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, '.': 27, ' ': 28,
        ',': 29, '!': 30, '?': 31
    }

    return [encoding_map[char] for char in message.lower()]
def rsa_encrypt(plaintext, public_key, n):
    # Convert the plaintext into an integer
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')

    # Encrypt the plaintext using the public key
    ciphertext = pow(plaintext_int, public_key, n)
    return ciphertext


# Public key components
n= 1271
public_key = 17
# Message to encrypt
message = "best course,8/10 and should maybe reduce the assignments please"

# Encrypting the message
encrypted_message = rsa_encrypt(message, public_key,n)
print(f"Encrypted message: {encrypted_message}")