from Crypto.Util.number import *


def pkcs_strip(a):
    last_byte = a[-1]
    if a[-int(last_byte) :] == long_to_bytes(4) * int(last_byte):
        return a[: -int(last_byte)]
    else:
        return "PaddingError"


print(pkcs_strip(b"ICE ICE BABY\x04\x04\x04\x04"))  # b'ICE ICE BABY'

print(pkcs_strip(b"ICE ICE BABY\x05\x05\x05\x05"))  # PaddingError
print(pkcs_strip(b"ICE ICE BABY\x01\x02\x03\x04"))  # PaddingError

