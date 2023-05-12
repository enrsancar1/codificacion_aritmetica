from decimal import *

def fixToBin(num, exp_max):

    bit_string = ""

    for exp in range(1, exp_max+1):
        if(num > Decimal(1/Decimal(2**exp))):
            num = num - Decimal(1/Decimal(2**exp))
            bit_string += '1'
        else:
            bit_string += '0'

    return bit_string

#bit_string = fixToBin(high, exp_max)
#print(bit_string)

def binToFix(num):
    exp_max = len(num)

    fix = 0
    for exp in range(len(num)):
        if(num[exp] == '1'):
            fix += Decimal(1/Decimal(2**(exp+1)))

    return fix

#num = binToFix(bit_string)
#print(num)

def minFix(high, low):
    
    antiguo = ""

    while(binToFix(high) > binToFix(low)):
        antiguo = high
        high = high[:-1]

    print("Longitud mínima:", len(antiguo), "bits")
    return binToFix(antiguo), antiguo
