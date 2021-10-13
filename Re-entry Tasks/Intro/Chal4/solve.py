from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import math

f = open('crypto\Re-entry Tasks\Re-entry Tasks\Intro\Chal4\pub.pem','r')
key = RSA.importKey(f.read())
n = (key.n)
e = (key.e)
ct = bytes.fromhex('3135b04822f3eaadb3cef509f214f42c9e9e5c18a68565dc435e5f67e626398fb7d49bd31ca10d738c4ccd78610d1b2f522becf312483bd2a1ab7bdbf73338e847c751021bada55fa4a071dbb726d1f127dd439577251862a25dac562ba110be9350fb461dffc772c8cc6cbe8aff79d860882ebd4f768e6442e2f1f9f4bb83f9')
ct = bytes_to_long(ct)

# p(p+2) = n => p**2 + 2p -n = 0
#solving for p

det = math.isqrt(2**2 + 4*n)
p = (-2 + det)//2
q = n // p

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
pt = long_to_bytes(pow(ct, d, n))
print(pt)