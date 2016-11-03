from Cryptodome.Cipher import AES
import hashlib

password = 'password' # Enter password here
key = hashlib.sha256(password.encode('utf-8')).digest()
mode = AES.MODE_EAX
nonce = #Enter nonce from aes-eax-ciphertext.txt here
tag = #Enter tag from aes-eax-ciphertext.txt here
ciphertext = #Enter ciphertext from aes-eax-ciphertext.txt here

decryptor = AES.new(key, mode, nonce)
plain = decryptor.decrypt_and_verify(ciphertext, tag) # Enter encrypted text here


with open("aes-eax-plaintext.txt", "w") as textfile:
	print("Decrypted text: ", plain, file=textfile)
	
print("Complete, check aes-eax-plaintext.txt for output")
