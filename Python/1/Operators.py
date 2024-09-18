#Operator
#1. Assignment operator
a = 100
b = a
print(a)

#- Gán giá trị cho nhiều biến trong cùng 1 câu lệnh
a, b, c = 100, 200, 300
print(a, b, c)

#- Hoán vị giá trị trong 2 biến
a = 3
b = 1
a, b = b, a
print(a, b)

#2. Arithmetic operator:
print(100 + 200)
print(200 - 100)
print(100 * 200)
print(100 / 200)
print(300 // 200)
print(15 % 2)
print(2 ** 10)

#3. Comparison operator:
#- Kết quả trả về là True hoặc False
print(100 == 100)
print(200 > 300)
print(200 < 300)
print(200 >= 300)
print(100 <= 30)
print(100 <= 30)
print(100 != 30)

#4. Logical operator;
print((20 == 20) and (1 < 0))
print((10 < 20) or (20 == 50))
print(not(20 == 20))

#5. Identity operator:
a = [1, 2, 3]
b = [1, 2, 3]
#- Trả về True nếu là 2 đối tượng giống nhau
print(a is b)

#- Trả về False nếu là 2 đối tượng khác nhau
print(a is not  b)

#6. Membership operator:
a = 'dangcapvjppro'
print('dangcap' in a)
print('gavl' in a)
