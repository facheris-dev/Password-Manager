from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib


# Warning
# Vulnerable to attacks like padding oracle attacks, chosen-plaintext attacks, and chosen-ciphertext attacks if the initialization vector isn’t changed for every encryption.
class AES_CBC:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.block_size = AES.block_size

    def encrypt(self, plain_text):
        # Set IV to protect against attacks
        # Pad our plain_text to fit the block size
        initialization_vector = get_random_bytes(self.block_size)
        padded_plain_text = pad(plain_text, self.block_size)
        block_cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector) 
        return initialization_vector + block_cipher.encrypt(padded_plain_text)
               
    def decrypt(self, cipher_text):
        # Get the iv from the cipher_text
        initialization_vector = cipher_text[:self.block_size]
        cipher_text_data = cipher_text[self.block_size:]
        block_cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector)
        return unpad(block_cipher.decrypt(cipher_text_data), self.block_size)         
