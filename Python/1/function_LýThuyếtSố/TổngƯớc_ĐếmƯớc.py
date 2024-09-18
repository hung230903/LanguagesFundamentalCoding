#Tính tổng ước và đếm ước của 1 số: Duyệt tới căn 2 của n

from math import *

def countSub(n):
    cnt = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i == n//i:
                cnt += 1
            else:
                cnt += 2
    return cnt

def sumSub(n):
    s = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i == n//i:
                s += i
            else:
                s += i + n//i
    return s

if __name__ == "__main__":
    n = int(input())
    print(countSub(n))
    print(sumSub(n))