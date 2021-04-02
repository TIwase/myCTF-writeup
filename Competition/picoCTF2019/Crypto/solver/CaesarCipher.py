# -*- coding: utf-8 -*-
import re
import sys

cipher = sys.argv[1]
# cipher = 'Ercy{ABC_abc}'
gap = range(0, 25)
for num in gap:
    outstr = ''
    for i in range(len(cipher)):
        # if re.search(cipher[i], symbo):
            # outstr = outstr + cipher[i]
        if ord(cipher[i]) < 65 or ord(cipher[i]) > 122:  # symbolic character
            outstr = outstr + cipher[i]
        elif ord(cipher[i]) > 90 and ord(cipher[i]) < 97:  # symbolic character
            outstr = outstr + cipher[i]
        elif ord(cipher[i]) < 65 + num: # capital character
            asc = ord(cipher[i]) + 26 - num
            outstr = outstr + chr(asc)        
        elif ord(cipher[i]) < 97 + num and ord(cipher[i]) > 96: # small character
            asc = ord(cipher[i]) + 26 - num
            outstr = outstr + chr(asc)
        else:
            asc = ord(cipher[i]) - num
            outstr = outstr + chr(asc)

    print("GAP =", num, ":")
    print(outstr)

