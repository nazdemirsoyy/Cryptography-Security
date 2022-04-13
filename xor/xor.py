a=  5  #0101
b = 3  #0011

result	= (a ^ b) #0110

print(result)

# Output
# 6 (0110)

############################################################################################################

import operator

print(operator.xor(5,3))
print(operator.xor(True,True))
print(operator.xor(True,False))
print(operator.xor(False,True))
print(operator.xor(False,False))

# Output
# 6
# False
# True
# True
# False

############################################################################################################

from random import seed
from random import random

def xor(text, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(text,key)])

cipherHex = '4c5c4117525f475e52195a4d'

#possibly from 10 up to 18
i = 10
for i in range(18):
    key = '2022-02-10 ' + str(i)
    seed(key)
    cipher = bytearray.fromhex(cipherHex).decode("utf-8")
    plain = xor(cipher, str(random())[2:])
    print("Case " + str(i) + ": " + plain)
