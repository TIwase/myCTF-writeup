# -*- coding: utf-8 -*-
import re
import sys

cipher = sys.argv[1]
symbo = '{}_'
gap = range(0, 25)
for num in gap:
    outstr = ''
    for i in range(len(cipher)):
        if re.search(cipher[i], symbo):
            outstr = outstr + cipher[i]
        elif ord(cipher[i]) == 32:  # white space
            outstr = outstr + cipher[i]
        elif ord(cipher[i]) < 65 + num: # capital letter
            asc = ord(cipher[i]) + 26 - num
            outstr = outstr + chr(asc)
        elif ord(cipher[i]) < 97 + num and ord(cipher[i]) >= 97: # small letter
            asc = ord(cipher[i]) + 26 - num
            outstr = outstr + chr(asc)
        else:
            asc = ord(cipher[i]) - num
            outstr = outstr + chr(asc)

    print("GAP =", num, ":")
    print(outstr)
    