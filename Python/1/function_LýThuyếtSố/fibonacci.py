#Số fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
#Kiểm tra 1 số có phải số fibo, in ra số fibo thứ n, in ra số fibo đầu tiên

from math import *

#In ra n số Fibo đầu tiên
def Fibo(n):
    if n == 1:
        print("0")
    elif n == 2:
        print("0 1")
    else:
        print("0 1 ", end = "")
        fn1, fn2 = 1, 0
        for i in range(2, n):
            fn = fn1 + fn2
            print(fn, end  = " ")
            fn2, fn1 = fn1, fn

#Kiểm tra 1 số có phải số Fibo
def checkFibo(n):
    if n == 0 or n == 1:
        return True
    
    fn1, fn2 = 1, 0
    for i in range(2, 100):
        fn = fn1 + fn2
        if fn == n:
            return True
    return False

#In ra số Fibo thứ n
def printFibo(n):
    if n == 0 or n == 1:
        return n
    
    fn1, fn2 = 1, 0
    for i in range(2, n + 1):
        fn = fn1 + fn2
        fn2, fn1 = fn1, fn
    return fn


if __name__  == "__main__":
    n = int(input())

    Fibo(n)
    print()

    if checkFibo(n):
        print("YES")
    else:
        print("NO")
    
    print(printFibo(n)) 