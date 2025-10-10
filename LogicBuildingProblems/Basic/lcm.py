def lcm(num1,num2):
    min_num= min(num1,num2)
    max_num = max(num1,num2)

    for i in range(max_num,num1*num2+1,max_num):
        if i%min_num==0:
            return i
    return num1*num2

def gcd(num1,num2):
    divisor = float("-inf")
    limit= num1 if num1<num2 else num2
    for i in range(2,limit+1):
        if num1%i==0 and num2%i==0:
            divisor = i if divisor<i else divisor
    return divisor



print(lcm(5,11))
print(lcm(10,5))