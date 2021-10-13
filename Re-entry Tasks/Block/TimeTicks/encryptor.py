from Crypto.Cipher import AES
from secret import flag
import time
from hashlib import md5


key = md5(str(int(time.time()))).digest()
padding =chr(16 - len(flag) % 16)
aes = AES.new(key, AES.MODE_ECB)
outData = aes.encrypt(flag + padding * ord(padding))
print(outData.encode('base64'))
