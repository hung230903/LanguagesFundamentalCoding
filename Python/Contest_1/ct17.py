"""
Cho một kí tự, bạn hãy kiểm tra kí tự nhập vào là chữ cái in hoa, in thường, 
chữ số hay kí tự đặc biệt(các kí tự không phải là chữ cái và chữ số)
"""

c = input()

if c.islower():
    print("LOWER")
elif c.isupper():
    print("UPPER")
elif c.isdigit():
    print("DIGIT")
else:
    print("SPECIAL")