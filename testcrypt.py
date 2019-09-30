#! /usr/bin/env python3

from cryptography.fernet import Fernet
import os

def write_key(keyfile):
    '''
    Generates a key and saves it to a file
    '''
    key = Fernet.generate_key()
    with open(keyfile, "wb") as key_file:
        key_file.write(key)
    return key


def load_key(keyfile):
    '''
    Load a key created previously
    '''
    return open(keyfile, "rb").read()


def encrypt_file(filename, key):
    '''
    Given a filename and key, encrypt the file and write to a new file
    '''
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + '.enc', "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key, target=None):
    ''' 
        Given the original filename and key, decrypt the file,
        possibly writing it to a new location
    '''
    if target == None:
        target = filename

    f = Fernet(key)

    with open(filename + '.enc', 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(target, "wb") as file:
        file.write(decrypted_data)


key = write_key("testcrypt.key")
f = Fernet(key)

message = "This is the protected message".encode()
encrypted = f.encrypt(message)

print(message)
print(encrypted)

# and reverse the process:

decrypted = f.decrypt(encrypted)
print(decrypted)


encrypt_file("testcrypt.py", key)
decrypt_file("testcrypt.py", key, target="testcrypt_compare.py")
