# greatest common divisor
def gcd(num1,num2):
    divisor = float('-inf')
    lp_len= num1 if num1<num2 else num2
    for i in range(2,lp_len+1):
        if num1%i==0 and num2%i==0:
            divisor = i if divisor<i else divisor
        
    return divisor

print(gcd(20,28))
print(gcd(60,36))

