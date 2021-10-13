from Crypto.Util.number import *

n = 78947048749078921553533397168223306327077414586183944609818553584663665747677757164091069731707888197818123265891690348381736231229561730395657333262905613958377739828118875586000068815867354664296956931106342366972209987312006882239420435532019823504851246162228112328268031305782869824549589268029030234941
e = 65537
ct = int('190400328f5de054f9441b3bcc880b6f1b8cbcf9b0ec7200adb77df3aeeb3a078a56d7c292dfca4bfcedfd5d04baacbdd0ef7e09abedee4bd019d558fe8dceb4992470de5a91f0cae31474d533b913f1fac6af8ef90e7c48cd997a54cfb116535dc2f0c899da7164ca42cc81b3e1b0f62000ef0c84e4562baef1735cf4f2f5e7',16)

dp = 8321799485573394942860161613115645956831906109530714384373208626667653915259713390904176783594390723717464276624389144661507957436413671900779232689662021
dq = 2198929330929270024294269318575741752298983645094723246081092280962552792055470240383972603201186261174772783400859274241718426034485142439904994069255041


for k in range(2,e):
    p = (e*dp-1 +k) //k
    if n%p ==0:
        l=p
        print(l)
        break

p=l
q=n//p
pt = long_to_bytes(pow(ct,inverse(e,(p-1)*(q-1)),n))
print(pt)