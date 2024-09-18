'''
Cho phương trình ax^2 + bx + c = 0. Hãy giải phương trình bậc 2 trên.
- Nếu phương trình vô nghiệm thì in ra "VO NGHIEM"
- Nếu phương trình vô số nghiệm thì in ra "VO SO NGHIEM"
- Nếu phương trình có 1 nghiệm hoặc nghiệm kép thì in ra 1 nghiệm duy nhất đó, 
    trường hợp có 2 nghiệm thì in ra nghiệm nhỏ hơn trước. Các nghiệm được in ra với 2 số sau dấu phẩy.

Chú ý chia ra 2 trường hợp a = 0, a != 0
'''

from math import *

a, b, c = map(int, input().split())

delta = b*b - 4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print("VO SO NGHIEM")
        else:
            print("VO NGHIEM")
    else:
        x = -c / b
        print("%.2f" % x)
else:
    if delta < 0:
        print("VO NGHIEM")
    elif delta == 0:
        x = -b / (2*a)
        print("%.2f" % x)
    else:
        x1 = (-b - sqrt(delta)) / (2*a)
        x2 = (-b + sqrt(delta)) / (2*a)
        x1 = min(x1, x2)
        x2 = max(x1, x2)
        print("%.2f" % x1, end = ' ')
        print("%.2f" % x2, end = ' ')