from Crypto.Cipher import Blowfish
from Crypto.Cipher import AES
import hashlib

password = 'password' # Enter password here
key = hashlib.sha256(password.encode('utf-8')).digest()
ivbf = b'\xd7\xebp6\xd3}E\xd4' # Blowfish initialization vector here
ivaes = b'b\xf1\x8a\x0fH\x01\xfcn\x00\xcd^\xe3\x19\xa1L\x17' # AES initialization vector here
mode1 = Blowfish.MODE_CFB
mode2 = AES.MODE_CFB

decryptor1 = Blowfish.new(key, mode1, IV=ivbf)
decryptor2 = AES.new(key, mode2, IV=ivaes)
plain1 = decryptor1.decrypt(b'=\x18\x1d\\') # Encrypted text here
plain2 = decryptor2.decrypt(plain1)

print("Decrypted text: ", plain2)
