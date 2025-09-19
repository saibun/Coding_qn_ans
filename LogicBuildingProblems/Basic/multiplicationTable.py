def multiFunc(num):
    for i in range(11):
        print(i*num) 


def recursiveMethod(num,i):
    if i==11:
        return
    print(num,"*",i,"=",num*i)
    i+=1
    recursiveMethod(num,i)

if __name__ == "__main__":
    # multiFunc(2)
    recursiveMethod(2,1)