
This is a writeup for You either know, XOR you don't task in GENERAL/XOR from cryptohack.org

we are given a hex string ```0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104```,

and there was no key.

But as the first part of the plaintext is supposed to be "crypto{" , so I XORed first 7 bytes with each of the seven digits 

of the known plaintext to find the key.

The result turned out to be ```myXORke```
it looked incomplete, and after adding making it ```myXORkey``` AND trying to decode the ciphertext,

the plaintext was returned.



from pwn import xor
from Crypto.Util.number import bytes_to_long

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_byte = bytes.fromhex(cipher_hex)
plain_format = "crypto{"

key = ''
for i in range(7):
    kz = xor(cipher_byte[i], ord(plain_format[i]))
    key += chr(bytes_to_long(kz))           
key += 'y'                              #The key looks to be "myXORke.." so i tried decoding by adding 'y'

print(xor(cipher_byte, key))
