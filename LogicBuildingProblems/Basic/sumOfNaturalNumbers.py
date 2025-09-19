def sumAll(num):
    if num == 1:
        return 1
    return num+sumAll(num-1)

# Formula to add first n numbers is (n*(n+1))/2
def formulaBased(num):
    return (num*(num+1))//2

if __name__ == "__main__":
    # print(sumAll(10))
    print(formulaBased(10))