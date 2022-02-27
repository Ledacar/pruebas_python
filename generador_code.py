import random

# Elementos que tendra la pass
minus = 'V'
mayus = minus.upper()   
simbolos = '-'
codenum = 0

for _ in range(3):
    code = random.choice(minus)
    codenum += 1
    base = code + simbolos + str(codenum)