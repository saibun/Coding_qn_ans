def gcd(a,b):
    lp_len = a if a<b else b
    divisor = float("-inf")
    for i in range(2,lp_len+1):
        if a%i==0 and b%i==0:
            divisor = i if divisor<i else divisor
    return divisor

def twoFactoradd(arra, arrb):
    den = (arra[1]*arrb[1]) // gcd(arra[1],arrb[1])
    num = (arra[0]*(den//arra[1]))+(arrb[0]*(den//arrb[1]))

    comm = gcd(num,den)
    den = den//comm
    num=num//comm

    return [num,den]

print(twoFactoradd([1,2],[3,2]))
print(twoFactoradd([1,3],[3,9]))
print(twoFactoradd([1,5],[3,15]))





    
