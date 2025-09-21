def reverseNum(num):
    reverse=""
    while(num>0):
        reverse += str(num%10)
        num=num//10
    return reverse
    



print(reverseNum(12345))


