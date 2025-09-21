def checkPower(x,y):
    result =x
    if x== 1:
        return False
    if y == 1:
        return True
    while result<=y:
        result = result*x
        if result == y:
            return True
    return False

print(checkPower(10,1))
print(checkPower(1, 20))
print(checkPower(2, 30))


