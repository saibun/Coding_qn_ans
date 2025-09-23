def pairCube(n):
    count=0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if i**3+j**3 ==n:
                count+=1
        
    return count

print(pairCube(9))
print(pairCube(28))

