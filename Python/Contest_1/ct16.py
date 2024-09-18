"""
Cho kí tự là chữ cái in hoa hoặc in thường
    , in ra kí tự kế tiếp sau nó trong bảng chữ cái ở dạng in thường
    , tức là kí tự nhập vào ở dạng in hoa hay in thường thì bạn đều in ra kí tự kế tiếp nó nhưng ở dạng in thường. 
Coi kí tự kế tiếp của của chữ Z là chữ A.
"""

"""
A -> Z: 65 - 90
a -> z; 97 - 122
0 - 9: 48 - 57
"""

n = input()

if n == 'z' or n == 'Z':
    print('a')
else:
    tmp = ord(n) #ord(): chỉ ra định dạng ASCII của kí tự
    tmp += 1
    print(chr(tmp).lower()) #chr(): chỉ ra định dạng kí tự của số nguyên