from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
import hashlib

password = 'password'
key = hashlib.sha256(password.encode('utf-8')).digest()
ivaes = Random.new().read(AES.block_size)
ivbf = Random.new().read(Blowfish.block_size)
mode1 = AES.MODE_CFB
mode2 = Blowfish.MODE_CFB
encryptor1 = AES.new(key, mode1, IV=ivaes)
encryptor2 = Blowfish.new(key, mode2, IV=ivbf)

text = 'text'
ciphertext1 = encryptor1.encrypt(text)
ciphertext2 = encryptor2.encrypt(ciphertext1)

with open("aes-blowfish-ciphertext.txt", "w") as textfile:
	print("Initialization vector AES: ", ivaes, file=textfile)
	print("Initialization vector Blowfish: ", ivbf, file=textfile)
	print("Encrypted text: ", ciphertext2, file=textfile)
	print("", file=textfile)
	print("Plug these values into aes-blowfish-decrypt.py to decrypt", file=textfile)
	
print("Complete, check aes-blowfish-ciphertext.txt for output")
