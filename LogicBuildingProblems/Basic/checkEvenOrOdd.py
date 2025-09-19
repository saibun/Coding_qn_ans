def checkEvenOrOdd(num):
    if num%2 == 0:
        return True
    else:
        return False

def bitwiseApproch(num):
    if (num & 1) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    if bitwiseApproch(10109):
        print("Even")
    else:
        print("Odd")


