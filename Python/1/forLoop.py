"""
for var in iterable:
    statement
    statement
    ...
else:
    statement
    ...

range(start, stop, step)
start: giá trị ban đầu, mặc định = 0
stop: giá trị cuối cùng
step: bước nhảy của dãy
"""
#Ex1
a = range(1, 10, 1)
for i in a:
    print(i, end = " ")

print("\n---")
#Ex2
for i in range(1, 10, 2):
    print(i, end = " ")

print("\n---")
#Ex3
for i in range(10):
    print(i, end = " ")

print("\n---")
#Ex4
for i in range(20):
    print(i, "lmao")

print("\n---")
#tính tổng S(n) = 1 + 2 + 3 +...+ n
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
print(s)

print("\n---")
#tính tổng S(n) = 1^2 + 2^2 + 3^2 +...+ n^2
s = 0
for i in range(1, n + 1):
    s += i**2
print(s)

print("\n---")
#tính tích các giai thừa A(n) = 1!.2!.3!...n!
s = 1
for i in range(1, n + 1):
    s *= i
print(s)

print("\n---")
#thay đổi biến i trong vòng for ko làm thay đổi biến i trả về trong vòng for, biến i trong vòng for chỉ phụ thuộc vào hàm range()
for i in range(1, 9):
    print(i)
    i += 2

print("\n---")
#forLoop với else
for i in range(1, 9):
    print(i)
else:
    print("END")

print("\n---")
#forLoop với break
for i in range(1, 21):
    print(i, end = ' ')
    if i % 7 == 0:
        break
    print('Lmao')

print("\n---")
#forLoop với continue
for i in range(1, 9):
    if i == 3:
        continue
    print(i)

print("\n---")
#nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(1, 10, 0):
    print(i)