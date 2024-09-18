#Kiểm tra số nguyên tố

from math import *

def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())

    if checkPrime(n):
        print("YES")
    else:
        print("NO")

    t = int(input())
    for i in range(1, t + 1):
        if checkPrime(i):
            print(i, end = " ")


