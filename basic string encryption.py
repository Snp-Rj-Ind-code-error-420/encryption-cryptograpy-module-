# raja op

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
'''msg=msg.encode()
key=key.encode()'''
iv = os.urandom(16)

def has(key):
    
    digest = hashes.Hash(hashes.SHA256())
    digest.update(key)
    key=digest.finalize()
    return key
    

    
def encrypt(msg,key,iv):
    

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    msg = padder.update(msg) + padder.finalize()
    print("padd msg",msg)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    msg = encryptor.update(msg) 
    encryptor.finalize()
    return msg

    
def decrypt(data,key,iv):
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    data = decryptor.update(data)
    decryptor.finalize()
    print("dec pad msg",data)
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(data) + unpadder.finalize()
    return data

msg="hello there we are here"
key="pass"
msg=msg.encode()
key=key.encode()
print('encode',msg)
print('encode',key)


''' hashing key  '''
key=has(key)

print("#key",key)

''' padding message and then encryption '''
data=encrypt(msg,key,iv)
print("see enc",data)

''' decryption and then unpadding '''
let_see=decrypt(data,key,iv)

print("see dec",let_see)
