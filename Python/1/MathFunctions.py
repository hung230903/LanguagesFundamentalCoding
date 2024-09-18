from math import *

#thông tin của thư viện math: print(help(math))
#math function
print('math function')

#sqrt(): square root(căn bậc 2), gía trị trả về là float
print('sqrt: ')
print(sqrt(36))
print('---')

#isqrt: interger square root, chỉ trả về giá trị nguyên
print('isqrt: ')
print(isqrt(29))
print('---')

#pow: power(lũy thừa), giá trị trả về là float
print('pow: ')
print(pow(2, 10))
print(pow(27, 1/3))
print('---')

#ceil: ceiling(): làm tròn lên, giá trị trả về là int
print('ceil: ')
print(ceil(2.3))
print(ceil(7.8))
print('---')

#floor(): làm tròng xuống, giá trị trả về là int
print('floor: ')
print(floor(2.3))
print(floor(7.8))
print('---')

#factorial(giai thừa)
print('factorial')
print(factorial(10))
print('---')

#gcd(a, b): greatest common divisor(ước chung lớn nhất)
print('gcd: ')
print(gcd(100, 450))
print('---')

#comb(n, k): combination(tổ hợp)
print('comb: ')
print(comb(10, 2))
print('---')

#perm(n, k): permutation(chỉnh hợp)
print(perm(5))

#fabs(): trị tuyệt đối
print('fabs: ')
print(fabs(-123.123))
print('---')

#Built-in function
print('Built-in function')
#abs(): trị tuyệt đối
print('abs: ')
print(abs(-12))
print('---')

#round(): làm tròn toán học
print('round: ')
print(round(2093.6231))
print(round(2093.12231))
print('---')

#max()/min()
print('max/min')
print(max(1,2, 3, 4, 5, 6))
print(min(1,2, 3, 4, 5, 6))
print('---')

#sum()
print('sum: ')
print(sum([1, 2, 3, 4, 5]))