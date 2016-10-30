from Crypto import Random
from Crypto.Cipher import AES
import hashlib

password = 'password'
key = hashlib.sha256(password.encode('utf-8')).digest()
iv = Random.new().read(AES.block_size)
mode = AES.MODE_CFB
encryptor = AES.new(key, mode, IV=iv)

text = 'text'
ciphertext = encryptor.encrypt(text)

with open("aes-ciphertext.txt", "w") as textfile:
	print("Initialization vector: ", iv, file=textfile)
	print("Encrypted text: ", ciphertext, file=textfile)
	print("", file=textfile)
	print("Plug these values into aes-decrypt.py to decrypt", file=textfile)
	
print("Complete, check aes-ciphertext.txt for output")
