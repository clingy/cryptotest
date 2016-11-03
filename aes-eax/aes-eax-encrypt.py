from Cryptodome.Cipher import AES
import hashlib

password = 'password'
key = hashlib.sha256(password.encode('utf-8')).digest()
mode = AES.MODE_EAX
encryptor = AES.new(key, mode)
text = 'text'
ciphertext, tag = encryptor.encrypt_and_digest(text.encode('utf-8'))

with open("aes-eax-ciphertext.txt", "w") as textfile:
	print("nonce = ", encryptor.nonce, file=textfile)
	print("tag = ", tag, file=textfile)
	print("ciphertext = ", ciphertext, file=textfile)
	print("", file=textfile)
	print("Plug these values into aes-eax-decrypt.py to decrypt", file=textfile)
	
print("Complete, check aes-eax-ciphertext.txt for output")
