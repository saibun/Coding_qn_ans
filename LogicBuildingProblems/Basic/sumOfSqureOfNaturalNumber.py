def sumSqureNaturalNum(num):
    # total=0
    # for i in range(num+1):
    #     total=total+(i*i)
    # return total
    # or
    return sum([i**2 for i in range(1,num+1)])

def recurciveApproch(num):
    if num ==1:
        return 1
    return num*num+recurciveApproch(num-1)
# Formula of sum of first n number's squre is n*(n+1)(2n+1)/6
def mathApproch(num):
    return num*(num+1)*(2*num+1)//6

# print(sumSqureNaturalNum(8))
# print(recurciveApproch(8))
print(mathApproch(10))