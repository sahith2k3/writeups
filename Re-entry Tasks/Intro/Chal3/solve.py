from Crypto.Util.number import *
from encrypt import e, n
import gmpy2
from math import isqrt

ct = ['31c2fbff33dec7b070cf737c57393c8ab9982ae51b87b64d001a00aa74264254159e81e13b82ac5bc4d7f38aead06fabbf5b21ee668700a44673fac75bc09b084e79513ada3d11b248ae5fca74ba0c2f807e73052f3090ee61a3bd226e14f4b0544f952449623b8cbd01cc42ff5462c4904d0c28af6dbce73596de45279461fd', '06c12db6573d6f6e1b2ecdaff825c6369da39fa7568f63cb6943070af8a3643e603493e23917833261f9c247d504455f3ef0e637d5f18ad2eeb5293ec0bb622bb171802a8d994b27a274c7dc417e247672b27bffb3dba25ea8dabb7379a58dd41704b605baf123046a88b4c5d5c238a6fae10007c28e482f84568c20f39d8bd7', '5ec536c327efe1a8432e4d36b76227ccebb15d73a102689ba24f7aadbd99298b17a63ee0396c4c489201e10e224f493364b8d999258ad507039520dfddca559c4c26eddc331fc3cf3dda65695aa5c8316423b57f35f641a7154771cd6735f1e8e6b1b212542bc6c21f5323e127447e07ef2cd5584f6a41eeef6b6e1c652b385e', '6488452ed101d5261f29924c5f5a6d3c5ecde3ea7e7ed235aa9c5f62b95dcadaaf2918a9085477d01536478fa747e2ab953b5ae4b56d1e8c074748e98db8fe2672c99720dcd0c968e31ceab02a532715c7f11b8c25384c406202b654d9ccaedcc0a2b017cee63285ae7d22a0c8a0da527e175b1dd042031eb6f9c1ef7dfd5e04']
ct = [bytes_to_long(bytes.fromhex(i)) for i in ct]

#factors of n[0] from factor[db]
p = 11196022518013846406450257763680307528861440840633712357021019120934410373180406217919066924474450204377977943388931820832436504741695416094988192576484719
q = 12842628342881595757040401293001010042980748144135693298042173293838412888189807594471962376219590606232699559767631407513176187065045811465165682366505527

phi = (p-1)*(q-1)

d = pow(e[0]//2, -1, phi)

pt = isqrt(pow(ct[0], d, n[0]))
print(long_to_bytes(pt))

# flag = "crypton{s0_y0u_f1nally_g07_GCD}"