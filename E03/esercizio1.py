import sys
import math
import numpy as np

n = input("Scrivi un numero intero: ")
m = input("Scrivi un altro numero intero: ")
nn = int(n)
mm = int(m)
print(bin(nn), bin(mm))
print(hex(nn), hex(mm))
ris_and = nn & mm
ris_or = nn | mm
print(bin(ris_and), bin(ris_or))
print(hex(ris_and), hex(ris_or))



