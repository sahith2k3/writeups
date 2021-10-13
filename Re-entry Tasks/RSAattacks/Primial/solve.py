from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from base64 import b64decode

f = open("crypto\Re-entry Tasks\RSAattacks\Primial\pub.pem", "r")
key = RSA.importKey(f.read())

ct = open("crypto\Re-entry Tasks\RSAattacks\Primial\\flag.enc", "r").read()
ct = b64decode(ct)
ct = bytes_to_long(ct)

phi = key.n - 1
d = pow(key.e, -1, phi)

pt = long_to_bytes(pow(ct, d, key.n))
print(pt)

#flag = Flag{S1nGL3_PR1m3_M0duLUs_ATT4cK_TaK3d_D0wn_RSA_T0_A_Sym3tr1c_ALg0r1thm}