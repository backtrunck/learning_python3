import re
import binascii
import struct

conj_hexa = { \
        "0":"0000", \
        "1":"0001", \
        "2":"0010", \
        "3":"0011", \
        "4":"0100", \
        "5":"0101", \
        "6":"0110", \
        "7":"0111", \
        "8":"1000", \
        "9":"1001", \
        "A":"1010", \
        "B":"1011", \
        "C":"1100", \
        "D":"1101", \
        "E":"1110", \
        "F":"1111"  }
    
        
num_hexa = raw_input("Digite o valor IEE754 em hexadecimal")
if re.match(r'^[0-9a-fA-F]+$',num_hexa) is None:
    print "\nHexadecimal Inválido\n"
    exit(1)
if len(num_hexa) <> 8 and len(num_hexa) <> 16:
    print "\nDigite um hexadecimal de 4 ou 8 bytes (8 ou 16 digitos hexadecimal)\n"
    exit(1)
valor = 0
bin = ""
print
for i in num_hexa.upper():

        bin += conj_hexa[i]

print "Hexadecimal:",num_hexa.upper()
print "Decimal (conv. direta):" ,int(bin,2)
print "binario:",bin
print "IEEE754\nSinal:", bin[0:1],"\nExpoente:",bin[1:9],"\nMantissa:",bin[9:]
if len(num_hexa) == 16:
    print "IEE754 Float: ",struct.unpack('<d', binascii.unhexlify(num_hexa))[0]
else:
    print "IEE754 Float: ",struct.unpack('<f', binascii.unhexlify(num_hexa))[0]


