#Tổ hợp chập k của n
#Tổ hợp chập 2 của n  = (n*(n-1))/2
from math import *

def combine(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    #hàm tổ hợp comb(n, k)
    print(comb(10, 2))

    n, k = map(int, input().split())
    print(combine(n, k))