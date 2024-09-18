#Số thuận nghịch/Số đối xứng/palindrome: 123321, 1221, 1111, 131, 22222, 2, 3 , 1

from math import *

def checkPalin(n):
    rev = 0
    tmp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    
    return rev == tmp

if __name__ == "__main__":
    n = int(input())

    if checkPalin(n):
        print("YES")
    else:
        print("NO")