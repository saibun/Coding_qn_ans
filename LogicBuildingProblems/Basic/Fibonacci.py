def fibonacci(indexPos):
    if indexPos<=1:
        return indexPos
    return fibonacci(indexPos-1)+fibonacci(indexPos-2)

def simpleFibonaci(count):
    left = 0
    right = 1
    print(f"{left} {right}",end=" ")
    for i in range (2,count):
        sum = left+right
        print(sum,end=" ")
        left = right
        right = sum
# print(fibonacci(5))
simpleFibonaci(10)

        

