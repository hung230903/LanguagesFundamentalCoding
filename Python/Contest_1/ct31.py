'''
Bizon the Champion gần đây đã có một món quà - một tủ kính mới với n kệ 
    và anh quyết định đặt tất cả những món quà của mình ở đó. 
Tất cả các món quà có thể được chia thành hai loại: huy chương và cúp. 
Bizon the Champion có a1 cúp giải nhất, a2 cúp giải nhì và a3 cúp giải ba. 
Bên cạnh đó, anh có b1 huy chương giải nhất, 
    b2 huy chương giải nhì và b3 huy chương giải ba. 
Đương nhiên, phần thưởng trong tủ phải sắp xếp cho thật đẹp, 
    đó là lý do Bizon the Champion quyết định tuân theo các quy tắc: 
        bất kỳ kệ nào cũng không thể chứa cả cúp và huy chương cùng một lúc; 
        không có kệ có thể chứa nhiều hơn 5 cúp; không có kệ có thể có hơn 10 huy chương. 
Giúp Bizon the Champion tìm hiểu xem có thể đặt tất cả các phần thưởng để tất cả các điều kiện được đáp ứng hay không.
'''

from math import *

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())

total_a = a1 + a2 + a3
total_b = b1 + b2 + b3

total_shelf_a = ceil(total_a / 5) 
total_shelf_b = ceil(total_b / 10)

if total_shelf_a + total_shelf_b <= n:
    print("YES")
else:
    print("NO")