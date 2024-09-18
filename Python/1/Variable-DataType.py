#Variable
#Trong python ko cần phải khai báo kiểu dữ liệu của biến
#   , biến sẽ được tạo và xác định kiểu tự động(dynamic typing) khi gán giá trị cho nó
#Cách đặt tên biến
    #Không chứa dấu cách, kí tự đặc biệt
    #Không bắt đầu bằng 1 chữ số
    #Tên biến trong python phân biệt in hoa và in thường(case sensitive)

#Để biết kiểu dữ liệu của biến thì dùng hàm type()
a = 100
print(type(a))

b = 2.55
print(type(b))

#Data Type
#1. Interger(Số nguyên)
#- Python ko giới hạn giá trị mà số nguyên có thể lưu        
a = 120938712904871290512740291348721309842170948
print(type(a))
print(a)

#- Python có thể in các số nguyên dưới dạng cơ số 10 nhưng
#   cũng có thể in ra dưới dạng cơ số 2, 8, 16
a = 0b1101
print(a)

b = 0o123
print(b)

c = 0x22A
print(c)
    
#2. Floating-point numbers(Số thực dấu phẩy động)
a = 28.128931251
print(type(a))
print(a)
#- Làm tròn phần thập phân
print('%.2f' % a)
print(round(a, 2))
print('{:.2f}'.format(a))

#- Trong python giá trị số thực có thể lưu lớn nhất xấp xỉ = 1.8*10^308
#   , các giá trị lớn hơn sẽ đc mô tả bằng chuỗi inf(infinity).
b = 3e5 #3.10^5
print(b)

c = 1.9e308
print(c)

#- Giá trị số thực nhỏ nhất  = 5.0*10^-342, các giá trị nhỏ hơn thì  = 0
d = 5.4e-325
print(d)

#3. Complex numbers(Số phức)
#- Bao gồm phần thực(real part) và phần ảo(imaginary part)
a = 2 + 3j
print(type(a))
print(a)

#- Cách lầy phần thực và phần ảo của số phức
print(a.real)
print(a.imag)

#4. Boolean(Kiểu đúng-sai)
#- Có 2 giá trị True Hoặc False
a = True
b = False
print(type(a))
print(a)
print(type(b))
print(b)

#- Các giá trị đc xác định là True khi: xâu != rỗng, số != 0
print(bool(100))
print(bool(0))
print(bool('lmao'))
print(bool(''))

#5. String(Xâu kí tự)
#- string đc đặt trong '' hoặc "" trên 1 dòng, trong trường hợp có nhiều dòng thì đặt giữa '''
s = 'lmao'
t = "aduvjp"
m = '''adu
ghe
z'''
print(s)
print(t)
print(m)

#6. Type Casting(Ép kiểu dữ liệu)
#- Quá trình casting trong Python đc hoàn thành bằng cách sử dụng constructor
#- Ép kiểu sang số nguyên 
a = int('123')
b = int(123.223)
print(a)
print(b)

#- Ép kiểu sang số thực 
a = float(50)
b = float('50.123')
print(a)
print(b)

#- Ép kiểu sang string
a = str(123)
b = str(123.123123)
c = str(True)
print(a)
print(b)
print(c)