Hello Guys,

This is a writeup to b_challenge4.docx from Tasks-Set-2

So started with exiftool and found nothing unusual. Then opened the docx file in word and found that there were unreadable content in it and the recogvered document showed a man holding guitar 

and with the text "We can't show you everything we have"

continuing with 
``` 
$ binwalk b_challenge.docx 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, name: docProps/
71            0x47            Zip archive data, at least v2.0 to extract, uncompressed size: 513, name: docProps/app.xml
457           0x1C9           Zip archive data, at least v2.0 to extract, uncompressed size: 731, name: docProps/core.xml
908           0x38C           Zip archive data, at least v2.0 to extract, name: _rels/
976           0x3D0           Zip archive data, at least v2.0 to extract, uncompressed size: 573, name: _rels/.rels
1282          0x502           Zip archive data, at least v2.0 to extract, name: word/
1349          0x545           Zip archive data, at least v2.0 to extract, name: word/_rels/
1422          0x58E           Zip archive data, at least v2.0 to extract, uncompressed size: 664, name: word/_rels/document.xml.rels
1751          0x6D7           Zip archive data, at least v2.0 to extract, uncompressed size: 208, name: word/settings.xml
2011          0x7DB           Zip archive data, at least v2.0 to extract, uncompressed size: 853, name: word/fontTable.xml
2392          0x958           Zip archive data, at least v2.0 to extract, uncompressed size: 2693, name: word/document.xml
3478          0xD96           Zip archive data, at least v2.0 to extract, uncompressed size: 2387, name: word/styles.xml
4207          0x106F          Zip archive data, at least v2.0 to extract, name: word/media/
4280          0x10B8          Zip archive data, at least v2.0 to extract, uncompressed size: 1785856, name: word/media/image1.jpeg
1766646       0x1AF4F6        Zip archive data, at least v2.0 to extract, uncompressed size: 39907, name: word/media/image2.jpeg
1806052       0x1B8EE4        Zip archive data, at least v2.0 to extract, uncompressed size: 1189, name: [Content_Types].xml
1807963       0x1B965B        End of Zip archive, footer length: 22
```

seemed like there were many fils hiding in there.


I extracted all of them using ```$ binwalk -dd='.*' b_challenge4.docx ``` and it extracted the files to '_b_challenge.docx.extracted' folder and then i extracted another

file called '0' inside this folder.

It had 3 more folders called ``` docProps   _rels   word```

Staying in the same folder I continued with 
```
$ egrep -r "flag" *
grep: word/media/image2.jpeg: binary file matches
```
So I cd to ```word/media/``` and use ```$ strings image2.jpeg| grep "flag" ``` to finally find the flag!

The Flag: ```flag{h0wz_the_joke_hahahha!!}```
