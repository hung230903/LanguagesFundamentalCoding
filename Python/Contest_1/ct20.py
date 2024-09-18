"""
Quảng trường Nhà hát ở thủ đô Berland có hình chữ nhật với kích thước n x m mét. 
Nhân dịp kỷ niệm thành phố, một quyết định đã được đưa ra để lát Quảng trường bằng những viên bằng đá granit vuông. 
Mỗi viên đá hình vuông có kích thước a x a.

Số lượng viên đá ít nhất cần thiết để lát Quảng trường là bao nhiêu? 
Nó được phép che phủ bề mặt lớn hơn Quảng trường Nhà hát. 
Nó không được phép phá vỡ các viên đá. 
Các cạnh của viên đá phải song song với các cạnh của Quảng trường.
"""

#c1:
n, m, a = map(int, input().split())

if n % a == 0 and m % a == 0:
    print((n//a) * (m//a))
elif n % a != 0 and m % a == 0:
    print((n//a + 1) * (m//a))
elif n % a == 0 and m % a != 0:
    print((n//a) * ((m//a) + 1))
elif n % a != 0 and m % a != 0:
    print((n//a +1)*(m//a + 1))

#c2:
n, m, a = map(int, input().split())

if n % a == 0:
    brick_n = n // a
else:
    brick_n = n // a + 1

if m % a == 0:
    brick_m = m // a
else:
    brick_m = m // a + 1

print(brick_n * brick_m)

