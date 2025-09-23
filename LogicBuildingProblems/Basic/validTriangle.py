def validTriangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        return "Valid Triangle"
    return "Invalid Triangle"

print(validTriangle(1,10,12))