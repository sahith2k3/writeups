Hello guys,
this is a writeup for SS_challenge4.png from set 2 tasks.

this image is a qr code.

with zbarimg...

```
$ zbarimg SS_challenge4.png 
QR-Code:C_F(n1, n2) = 14 * [C(n1,n2) / 14] + 7 * FLAG(n1,n2) + (C(n1,n2) mod 7)
```

I figured that this might be a misdirection, i used stegsolve to open the image in different planes, and found a different qr code in

red plane 0. which when scanned gave the flag

```
VolgaCTF{5t3g0_m4tr3shk4_in_4cti0n}
```
