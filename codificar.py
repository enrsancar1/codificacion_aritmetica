from decimal import *
import os
from freqs import getFrequencies
from number import fixToBin, minFix

with open("file.txt", "r") as file:
    cadena = file.read()

#cadena = "Esta cadena ha sido escrita para su compresión usando codificación aritmética. Enrique Sánchez Cardoso - Procesamiento Avanzado de Señales - ETSI"

intervalo = getFrequencies(cadena)

print(intervalo)

#CODIFICAR
getcontext().prec = 1
getcontext().traps[Rounded] = True

low = Decimal('0')
high = Decimal('1')

flag = False

for simbolo in cadena:
    rango = high - low

    while flag == False:
        try:
            low + rango * Decimal(intervalo[simbolo][1])
            low + rango * Decimal(intervalo[simbolo][0])
            flag = True
        except Rounded as e:
            getcontext().prec = getcontext().prec + 1

    high = low + rango * Decimal(intervalo[simbolo][1])
    low = low + rango * Decimal(intervalo[simbolo][0])
    flag = False

print("Cadena original:", cadena)
print("Rango codificado:", low, high)
print("Numero de bytes de la cadena:", os.stat('file.txt').st_size)

# Escribir en un fichero
getcontext().prec = 1000
getcontext().traps[Rounded] = False

import math

rango_final = high - low
exp_max = int(Decimal(-math.log2(rango_final)) + 1)

value, string_value = minFix(fixToBin(high, exp_max), fixToBin(low, exp_max))

print("Cadena codificada:", value)
print("Cadena binaria:", string_value)

from bit_io import write_bin
write_bin(string_value, "file_compressed")
