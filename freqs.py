from decimal import *

def getFrequencies(cadena):
    
    getcontext().prec = 4

    veces = {}
    for simbolo in cadena:
        veces[simbolo] = Decimal(cadena.count(simbolo))

    longitud = len(cadena)
    prob = {}
    for simbolo in veces:
        prob[simbolo] = str(veces[simbolo]/longitud)

    acum = 0
    intervalo = {}
    for simbolo in veces:
        intervalo[simbolo] = (str(acum), str(acum + Decimal(prob[simbolo])))
        acum = acum + Decimal(prob[simbolo])

    return intervalo