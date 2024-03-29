from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from secret import flag

while True:
	p = getPrime(512)
	q = p+2
	if isPrime(q):
		break
n = p*q
e = 65537
phin = (p-1)*(q-1)
assert GCD(e, phin) == 1

d = inverse(e, phin)

# Message/Flag to be encrypted
m = bytes_to_long(flag)
ciphertext = long_to_bytes(pow(m, e, n))
ciphertext = ciphertext.encode("hex")

obj1 = open("ciphertext.txt",'w')
obj1.write(ciphertext)

key = RSA.construct((n, e))
f = open("publickey.pem",'w')
f.write(key.exportKey("PEM"))
