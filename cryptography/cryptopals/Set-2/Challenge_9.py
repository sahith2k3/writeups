from Crypto.Util.number import *


def pkcs7_pad(text, size):
    pad_size = size - len(text)
    return text + long_to_bytes(pad_size) * pad_size


string = b"YELLOW SUBMARINE"
total_size = 20
padded_string = pkcs7_pad(string, total_size)
print(padded_string)
