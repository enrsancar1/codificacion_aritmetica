from bit_io import read_bin
from number import binToFix
from decimal import *
from freqs import getFrequencies

#DECODIFICAR
cadena = "Esta cadena ha sido escrita para su compresión usando codificación aritmética. Enrique Sánchez Cardoso - Procesamiento Avanzado de Señales - ETSI"
intervalo = getFrequencies(cadena)

cadena_deco = ""

getcontext().prec = 10000

bit_string = read_bin("file_compressed")
low = binToFix(bit_string)
print("Cadena codificada:", low)
print("Cadena binaria:", bit_string)

while len(cadena_deco) < len(cadena):
    for simbolo in intervalo:
        if(low >= Decimal(intervalo[simbolo][0]) and low < Decimal(intervalo[simbolo][1])):
            cadena_deco = cadena_deco + simbolo
            rango = Decimal(intervalo[simbolo][1]) - Decimal(intervalo[simbolo][0])
            low = low - Decimal(intervalo[simbolo][0])
            low = low / rango

print("Cadena decodificada:", cadena_deco)

if(cadena == cadena_deco):
    print("Exito")
else:
    print("Fracaso")

with open("file_decompressed.txt", "w") as file:
    file.write(cadena_deco)
