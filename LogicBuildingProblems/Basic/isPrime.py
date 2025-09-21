def isPrimeNum(num):
    for i in range(2,num-1):
        if num%i == 0:
            return "Not Prime"
    return "Prime"

print(isPrimeNum(15));
print(isPrimeNum(11));