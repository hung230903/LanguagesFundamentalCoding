#Nhập dữ liệu từ bàn phím
#input(): giá trị trả về ở kiếu str
a = input('Enter a number: ')
print(type(a))
print(a)

#- Ép dữ liệu nhập vào sang kiểu dữ liệu mong muốn
a = int(input('Enter a number: '))
print(type(a))
print(a)

#Eg:
a = int(input('Enter length: '))
b = int(input('Enter width: '))

p = 2 * (a + b)
s = a * b
print(p, s)

#map(): nhập nhiều dữ liệu trên cùng 1 dòng
a = input('Enter 3 numbers: ')
b = a.split()
x, y, z = map(int, b)
print(x)
print(y)
print(z)

#- Thu gọn:
a, b, c, d = map(int, input('Enter 4 numbers: ').split())
print(a + b + c + d)

a, b, c, d = map(float, input('Enter 4 numbers: ').split())
print(a, b, c, d)

