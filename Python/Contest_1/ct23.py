'''
Doremon muốn leo lên một cầu thang gồm n bước. 
Anh ta có thể leo 1 hoặc 2 bước mỗi lần di chuyển. 
Doremon muốn số lần di chuyển là bội số của một số nguyên m. 
Số lượng di chuyển tối thiểu làm cho anh ta leo lên đỉnh cầu thang thỏa mãn điều kiện của anh ta là gì?
'''

n, m = map(int, input().split())

if n % 2 == 0:
    step_min = n // 2
else:
    step_min = n // 2 + 1

ans = (step_min + m - 1) // m * m

if ans <= n:
    print(ans)
else:
    print("-1")
