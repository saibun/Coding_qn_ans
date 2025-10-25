def dTob(value):
    bn = []
    
    while value>0:
        bit = value%2
        bn.append(str(bit))
        value=value//2
    bn.reverse()
    opt = "".join(bn)
    return opt



print(dTob(12))