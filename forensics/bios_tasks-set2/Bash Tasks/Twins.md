Hello Guys,

this is the writeup for Twins task from Task Set 2.

The README file said 
```
I Hope These files are as same as twins. But find it yourself.

PS: You can you python if you want.
```

As the name and the hint suggested, I had to find the difference between these two..

So I used ``` $ cmp -l -b Twin1 Twin2``` , and got

```
2341267 104 D    151 i
2342443  50 (    156 n
2343437 160 p    143 c
2344514  42 "    164 t
2345325 227 M-^W 146 f
2346588 152 j    173 {
2347984 157 o    171 y
2349108 347 M-g   60 0
2350246 200 M-^@ 165 u
2351057 244 M-$  137 _
2352678 311 M-I  107 G
2353849 173 {    157 o
2355605  17 ^O   164 t
2355606 157 o    137 _
2356957 264 M-4  155 m
2358173 355 M-m   63 3
2359344 132 Z    175 }
```

Therefore getting the flag, ``` inctf{y0u_Got_m3} ```
