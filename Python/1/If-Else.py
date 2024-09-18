#Selection structure: cấu trúc rẽ nhánh
#if-else
a = 60
if a >= 50 and a <= 100:
    print('python')

b = 20
if b >= 50 and b <= 100:
    print('lmao')

print('---')

#Eg: 
print('Kiểm tra số chẵn')
a = int(input('Enter an interger: '))
if a % 2 == 0:
    print('Even number')
else:
    print('Odd number')

print('---')

print('Kiểm tra số lớn hơn/bé hơn')
a, b = map(int, input('Enter 2 intergers: ').split())
if a < b:
    print(a, 'less than', b)
elif a > b:
    print(a, 'greater than', b)
else:
    print(a, 'equal to', b)

#Toán tử 3 ngôi
a, b = 100, 200
res = 'lmao' if a < b else 'lol'
print(res)

#Nested if
print('Kiểm tra xem n có phải là số lớn hơn hoặc bằng 50 và chia hết cho 1 trong 3 số là 3, 5, 7')
n = 80
if n >= 50:
    if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print('YES')
else:
    print('NO')