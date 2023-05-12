from decimal import *

getcontext().prec = 10000

def write_bin(string_value, filename):
    original_string = string_value

    pad = 8 - len(original_string) % 8
    if(pad != 0):
        print("Insertamos un padding de:", pad, "bits")
        original_string =  original_string + '0' * pad

    # divido en chunks de 8 bits
    bit_strings = [original_string[i:i + 8] for i in range(0, len(original_string), 8)] 

    # los convierto a int
    byte_list = [int(b, 2) for b in bit_strings]

    print("Numero de bytes de la salida:", len(byte_list))

    with open(filename, 'wb') as f:
        f.write(bytearray(byte_list))

def read_bin(filename):
    with open(filename, 'rb') as f:
        bytes = f.read(1000)

        read_string = ""
        
        for byte in bytes:
            read_string += str(bin(byte))[2:].zfill(8)

        return read_string
