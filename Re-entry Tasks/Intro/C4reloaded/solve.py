from Crypto.PublicKey import RSA
from math import isqrt
from Crypto.Util.number import *

f = open('crypto\Re-entry Tasks\Intro\C4reloaded\pub.pem','r')
key = RSA.importKey(f.read())
n=(key.n)
e=(key.e)

ct = bytes.fromhex('10d4f78cb70069ef086b3e2c42b8e465c1ebf509c770e9d4f0177df154e0175690a6a9f4d5132dcdb89dde0e192f00215a7af701ec4fe112aedc9e35751b9bda2cff76ab119451f4f112d49c6a670f3ac82794663eb8df1ea9c3d379b840bf192c43be9a890a06bbf8f10b46fd9015e180b0ba14916de49a634ad8fac6b49f91')
ct = bytes_to_long(ct)

#p*(p+i)=n => p**2+i*p-n=0
i = 10000
while True:
    det = i**2 + (4*n)
    det = isqrt(det)
    p = (-i + det)//2
    q = n//p
    if n==p*q:
        break
    i += 1

phi = (p-1)*(q-1)
d = pow(e,-1,phi)
pt = pow(ct,d,n)

print(long_to_bytes(pt))