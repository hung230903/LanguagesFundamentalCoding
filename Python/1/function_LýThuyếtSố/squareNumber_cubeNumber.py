from math import *

def checkSquare(n):
    sqrt = isqrt(n)
    return sqrt * sqrt == n

def checkCube(t):
    cbrt = int(pow(t, 1/3))
    return cbrt**3 == t or ((cbrt + 1)**3 == t)

if __name__ == "__main__":
    n = int(input())

    if checkSquare(n):
        print("YES")
    else:
        print("NO")

    t = int(input())
    if checkCube(t):
        print("YES")
    else:
        print("NO")