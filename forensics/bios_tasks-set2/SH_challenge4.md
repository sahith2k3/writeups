Hello guys,

this is a writeup for SH_challenge4.jpg from tasks set 2.

So, the image had a picture of Bhagat singh and 'INQUILAB ZINDABAD' written on it.

So, I tried using exiftool and found nothing unusual. Even different planes on stegsolve didnt have any lead....

But when I used ```$ strings SH_challenge4.png```,

I found ```723fa61abce2c64e60f5f3a4c1426a15``` on the last line.

decryting this text with a MD5 decrypter online, ``` WEAREFREE ``` was returned.

assuming this might be some kind of a password...

SO Using ```$ steghide extract -sf SH_challenge4.jpg -p WEAREFREE```, 

```wrote extracted data to "vip.txt".``` was returned.

finally ```cat vip.text``` gave the flag ```inctf{H4pPy_Ind3p3nD3nC3_D4Y}```

