import random
from  werkzeug.security import generate_password_hash

# Elementos que tendra la pass
minus = 'abcdfghijklñnopkrstuvwxyz'
mayus = minus.upper()   
numeros = '0123456789'
simbolos = '!"·$%&/()=/*-@~#'

# Elementos unidos
base = minus + mayus + numeros + simbolos
longitud = 12

# Formar pass aleatorio
for _ in range(1):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_encript = generate_password_hash(password)
    print('==================')
    print('Pass')
    print(password)
    print('==================')
    print('encrypted password')
    print(password_encript)
    print('')