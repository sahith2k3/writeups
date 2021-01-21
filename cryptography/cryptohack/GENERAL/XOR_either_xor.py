from pwn import xor
from Crypto.Util.number import bytes_to_long

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_byte = bytes.fromhex(cipher_hex)
plain_format = "crypto{"

key = ''
for i in range(7):
    kz = xor(cipher_byte[i], ord(plain_format[i]))
    key += chr(bytes_to_long(kz))
key += 'y'

print(xor(cipher_byte, key))
