from pwn import xor
from Crypto.Util.number import bytes_to_long


cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_byte = bytes.fromhex(cipher_hex)


key= cipher_byte[0] ^ ord('c')

for i in cipher_byte:
    print(chr(bytes_to_long(xor(i, key))), end='')
print()
