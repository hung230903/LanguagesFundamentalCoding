"""
while condition:
    statement
    statement
    ...
else:
    statement
    statement
    ...
"""

#Ex1
n = 1
while n <= 5:
    print("adu", n)
    n += 1
else:
    print("END")

#Ex2
print("\n---")
n = 9
i = 1
while i <= n:
    print(i)
    i+=1

print("\n---")
#whileLoop với continue
n = 5
i = 1
while i <= n:
    print(i)
    continue
    i += 1    

print("\n---")
#whileLoop với break
n = 5
i = 1
while i <= n:
    print(i)
    if i == 3:
        break
    i += 1 

print("\n---")
#Yêu cầu user nhập vào số dương, nhập số 0 hoặc âm thì nhập lại
while True:
    n = int(input())
    if n > 0:
        break

print("\n---")
#Đếm số lượng chữ số
n = int(input())
cnt = 0
if n == 0:
    cnt = 1

while n != 0:
    cnt += 1
    n //= 10 
print(cnt)

print("\n---")
#Tổng số lượng chữ số
n = int(input())
s = 0
while n != 0:
    s += n % 10
    n //= 10
print(s)

print("\n---")
#Lật ngược số
n = int(input())
cvrt = 0
while n != 0:
    cvrt = cvrt * 10 + n % 10
    n //= 10
print(cvrt)
