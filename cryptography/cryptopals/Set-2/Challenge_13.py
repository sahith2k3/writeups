import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

uid = 1
key = random.randbytes(16)

def parse(a):
    list = a.split(b"&")
    out = {}
    for i in list:
        i = i.split(b"=")
        out[i[0].decode("utf-8")] = i[1].decode("utf-8")

    return out

def profile_for(a):
    global uid
    a = a.decode("utf-8")
    a.replace("&", "").replace("=", "")
    out = {}
    out["email"] = a
    out["uid"] = uid
    out["role"] = "user" 
    enc_out = f"email={a}&uid={uid}&role=user"
    return enc_out.encode()


def encrypt(a):
    global key
    return AES.new(key, AES.MODE_ECB).encrypt(pad(a, 16))

def decrypt(a):
    global key
    profile = unpad(AES.new(key, AES.MODE_ECB).decrypt(a), 16)
    return parse(profile)

if __name__ == "__main__":
    payload = b"easy@peasy.com"  #input of this length will push value of role to a seperate block
    pt = profile_for(payload)  #email=easy@peasy.com"&uid=1&role=user
    ct = encrypt(pt)           
    #we want to make it email=easy@peasy.com&uid=1&role=admin....
    #we can find the ct_block if pt_block is admin by giving input = easy@peasyadmin\x0b\x0b.... and cutting the second block from this ct

    payload = b"easy@peasy" + pad(b"admin&e=", 16)
    ct_ = encrypt(profile_for(payload))
    admin_ct_block = ct_[16: 32]

    ct_blocks = [ct[i:i+16] for i in range(0, len(ct)-16+1, 16)]
    # target blocks email=easy@peasy , .com&uid=1&role= , admin\x0b...... , .......

    final_ct = b"".join(ct_blocks[:2] + [admin_ct_block] + ct_blocks[2:])

    print(decrypt(final_ct))
