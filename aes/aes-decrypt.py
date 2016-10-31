from Crypto.Cipher import AES
import hashlib

password = 'password' # Enter password here
key = hashlib.sha256(password.encode('utf-8')).digest()
iv = b'\x9f\xea.\xa3\xb5\x8bT\x19\xaa&\xacR\xb7\xbc\xe4\x9c' # Enter initialization vector here
mode = AES.MODE_CFB

decryptor = AES.new(key, mode, IV=iv)
plain = decryptor.decrypt(b'\xe5\xb8\xb0\xe5') # Enter encrypted text here

print("Decrypted text: ", plain)
