#Số hoàn hảo/Perfect number

from math import *

#C1:
def perfect(n):
    s = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            if i == n //i:
                s += i
            else:
                s += i + n//i
    return s == n

#C2:
#Định lý euclid-euler
#Nếu p là số nguyên tố và 2^p - 1 cx là số nguyên tố -> (2^p - 1) * 2^(p-1) là số hoàn hảo

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def perfect_2(n):
    for p in range(2, 35):
        if prime(p):
            if prime(2**p - 1):
                if (2**p - 1) * (2**(p - 1)) == n:
                    return True
    return False

if __name__  == "__main__":
    n = int(input())

    if perfect(n):
        print("YES")
    else:
        print("NO")

    if perfect_2(n):
        print("YES")
    else:
        print("NO")