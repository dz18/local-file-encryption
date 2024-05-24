from Crypto import Cipher
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import *
import os

def generate_key(size, output_file_name):
    ''' Generate a random symmetric key '''
    if size in [16, 24, 32]:
        key = get_random_bytes(size)
        with open(output_file_name, 'wb') as f:
            f.write(key)
    else:
        print("Error: Invalid Key Size. Only sizes 16, 24, & 32 accepted.")

def get_key(source):
    ''' Get key from file '''
    with open(source, 'rb') as f:
        key = f.read()

    return key

def encrypt_file(source, key):
    ''''''
    with open(source, 'rb') as f:
        data = f.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded)

    with open(source + '.enc', 'wb') as f:
        f.write(iv + encrypted_data)

def decrypt_file(source, key):
    
    # Read CipherText
    with open(source, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Encrypt and Unpad
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_padded = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext_padded, AES.block_size)

    # Check if decrypted filename exist already
    name = ''
    if os.path.exists(source):
        name = source.strip(".enc")
        type = os.path.splitext(name)
        name = name.rstrip(type[1])
        name += '_dec' + type[1]

    # Save plaintext into new file
    with open(name, 'wb') as f:
        f.write(plaintext)

def test():
    key = get_key("test/key")
    encrypt_file('test/test-image.jpg', key)
    decrypt_file('test/test-image.jpg.enc', key)

