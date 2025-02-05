import rsa
def rsa_decrypt(ciphertext, private_key, n):
    # Decrypt the ciphertext using the private key
    plaintext_int = pow(ciphertext, private_key, n)

    # Convert the integer plaintext back to a string
    plaintext = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    return plaintext


# Example values (ciphertext and private key components)
ciphertext = 104977 # Example encrypted message (ciphertext) as an integer
private_key = 71 # Example private key exponent (d)
n = 1271  # Modulus (n)

# Decrypt the message
decrypted_message = rsa_decrypt(ciphertext, private_key, n)
print(f"Decrypted message: {decrypted_message}")