"""
Lý thuyết đồng dư:
1. (A + B) % C = ((A  % C) + (B % C) % C)
2. (A - B) % C = ((A % C) - (B % C) + C) % C
3. (A * B) % C = ((A % C) * (B % C)) % C
4. (A / B) % C = ((A % C) * (B^-1 % C)) % C -> Nghịch đảo modul
"""

#Khi bài toán yêu cầu chia dư kết quả cho 1 số nào đó => Tính đến đâu chia dư đến đó
from math import *

if __name__ == "__main__":
    
    #Tính n giai thừa % cho 10^9 + 7
    n = int(input())
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= (10**9 + 7)
    print(res % (10**9 + 7))

    #Tính a^b chia dư cho c
    a, b, c = map(int, input().split())
    res = 1
    for i in range(b):
        res *= a
        res %= c
    print(res)

