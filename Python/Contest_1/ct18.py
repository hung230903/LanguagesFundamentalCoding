"""
Cho kí tự c, nếu kí tự c là chữ cái in thường thì chuyển nó thành chữ cái in hoa tương ứng và ngược lại 
    nếu c là chữ cái in hoa thì chuyển nó thành chữ cái in thường tương ứng. 
Trường hợp kí tự nhập vào không phải là chữ cái thì không thay đổi nó.
"""

c = input()

if c.isupper():
    print(c.lower())
elif c.islower():
    print(c.upper())
else:
    print(c)