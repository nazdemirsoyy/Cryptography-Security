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
