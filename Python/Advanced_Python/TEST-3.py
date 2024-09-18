from random import *
from time import *

def p02(st,G):
  while G=='':
    G=str(input('Ta hỏi: %s'%st))
  return G

def s1(al,n):
  sum=0
  while n>0:
    sum= sum + n%10
    n= n//10
  while sum>9:
    sum=sum//10 + sum%10
  while sum>al:
    sum-=al
  return sum

print('                 oo0oo')
print('                o8888888o')
print('                88" . "88')
print('                (| -_- |)')
print('                 \  =  /')
print("              __/`---'\__")
print("            .' \\|     |// '.")
print('           / \\|||  :  |||// \ ')
print('          / _||||| -:- |||||- \ ')
print('          |   | \\\  -  /// |   | ')
print('           | \_|  ''\---/' '  |_/ | ')
print('          \  .-\__ "-"  ___/-. / ')
print("        _'. .'  /--.--\  `. .'_ ")
print("     ."" '<  `.___\_<|>_/___.' >' " ". ")
print('    | | :  - \.;`\ _ /`;.`/ - ` : | | ')
print('    \  \ _.   \_ __\ /__ _/   .- /  / ')
print("=====`-.____.___ \_____/___.-___.-'===== ")
print()
print("                  `=---='  ")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('              Xin quẻ của phật    ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

t = str(input('Con tên gì: '))
t = p02('Tên con là gì',t)
print('', 'Con muốn hỏi ta gì:', '1:Hôm nay', sep='\n')
print('2:Ngày mai', '3:Dự định', sep='\n')
print('4:Con phân vân gì đó', '5:Nhờ phật chọn dùm', sep='\n')
c = str(input('Con chọn đi:'))
while (c != '1') and (c != '2') and (c != '3') and (c != '4') and (c != '5'):
  c = str(input('Ta bảo con nhập stt ở trên:'))
p = s1(3,randint(1,100**9))
o = s1(3,randint(1,100**9))
u = s1(2,randint(1,100**9))
l3 = {1: 'Có ', 2:'Không chắc chắn lắm ', 3:'Không '}
l1 = {'1':'Ngày hôm nay ','2':'Ngày mai ',1:'Theo chiều huướng tốt rất tốt ',2: 'Chỉ tạm được thôi',3: 'Theo chiều hướng rất xấu khó suôn sẽ ','4': 'Mặc dù'}
if (c=='1') or (c=='2'):
  chon=l1.get(c)
  doan=l1.get(p)
  doan1=doan4=''
if c=='3':
  chon = str(input(' Dự định của con là gì: '))
  chon = p02('Dự định của con là gì:',chon)
  doan = l1.get(p)
  doan1 = doan4 =''
if c=='4':
  chon = str(input(' Con phân vân điều gì: '))
  chon = p02('Con phân vân điều gì:',chon)
  doan = l3.get(p)
  doan1 = l1.get('4')
  doan4 = l1.get(o)
if c=='5':
  chona1 = str(input(' phương án 1: '))
  chona1 = p02('Ta hỏi phương án 1 của con là gì:',chona1)
  chona2 = str(input(' phương án 2: '))
  chona2 = p02('Ta hỏi phương án 2 của con là gì:',chona2)
  l5={1:chona1,2:chona2}
  chon = l5.get(u)
  doan = l3.get(p)
  doan1 = l1.get('4')
  doan4 = l1.get(o)
print()
print('đang xin quẻ phật....');sleep(5)
print()
print('Ta thấy',"'",chon,"''",'của %s'%t,'có vẻ',doan,doan1,doan4)