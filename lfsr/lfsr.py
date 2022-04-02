#state = (1 << 127) | 1
#while True:
#    print(state & 1, end ='')
#    newbit = (state ^ (state >>1) ^ (state >>2) ^ (state >>7))
#   state = (state >> 1) | (newbit << 127)

##############################################################

#state = 0b1001
#for i in range(20):
#    print("{:04b}".format(state))
#    newbit = (state ^ (state >> 1)) & 1
#    state = (state >> 1) | (newbit)

##############################################################

def lfsr_generated(seed,mask,n):
    seed_int = int(seed,2)
    mask_int = int (mask,2)
    nbits = len(seed)

    state = seed_int
    while n > 0:
        output = 1 & state #get the most right bit

        _mask,_state,new_bit = mask_int ,state ,0
        while _mask:
            new_bit ^= (1 & _mask) * (1 & _state)
            _mask >>= 1
            _state >>= 1
        
        state = state >> 1 | new_bit << (nbits - 1)

        yield output, state
        n -= 1

seed ='0001'
mask ='0101'
samples = 20

key = lfsr_generated(seed,mask,samples)
key_str =''.join(str(x) for x, _ in key)
key_hex = hex(int(key_str,2))[2:]
