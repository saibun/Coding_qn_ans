def perfectNumber(num):
    sum=0
    for i in range(1,num-1):
        if num%i==0:
            sum+=i

    if sum == num:
        return True

    return False

print(perfectNumber(6))
print(perfectNumber(15))



