'''
Polycarp có ba chị em: Alice, Barbara và Cerene. Họ đang thu thập tiền xu. 
Hiện tại, Alice có một đồng tiền, Barbara có tiền xu và Cerene có tiền xu. 
Gần đây Polycarp đã trở về từ chuyến đi vòng quanh thế giới và mang theo n xu. 
Anh ta muốn phân phối tất cả n xu này giữa các chị em của mình 
    theo cách mà số lượng tiền Alice có bằng số lượng tiền mà Barbara có và bằng với số lượng tiền mà Cerene có. 
Nói cách khác, nếu Polycarp đưa A xu cho Alice, B xu cho Barbara và C xu cho Cerene (A + B + C = n)
    , thì a + A = b + B = c + C. 
Lưu ý rằng A, B hoặc C (số lượng tiền mà Polycarp đưa cho Alice, Barbara và Cerene tương ứng) có thể là 0. 
Nhiệm vụ của bạn là tìm hiểu xem có thể phân phối tất cả n xu giữa các chị em theo cách được mô tả ở trên không.
'''

a, b, c, n = map(int, input().split())

total = a + b + c + n

if total % 3 == 0 :
    money_each = total // 3
    if money_each >= a and money_each >= b and money_each >= c:
        print("YES")
    else:
        print("NO")
else:
    print("NO")