def withoutThird(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("a value is",a,"and b value is",b)

def builtInMethod(a,b):
    a,b=b,a
    print("a value is",a,"and b value is",b)

# withoutThird(1,2)
builtInMethod(10,100)