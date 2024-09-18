"""
Một ngày ở hành tinh 28Tech có 28 giờ, mỗi giờ lại có 28 phút và mỗi phút lại có 28s. 
Hiện tại đồng hồ tại hành tinh 28Tech đang ở h giờ và m phút, câu hỏi đặt ra là sau k phút nữa, 
đồng hồ sẽ là bao nhiêu giờ bao nhiêu phút. Khi in ra nếu giờ hoặc phút là số có 1 chữ số, bạn phải thêm số 0 vào đầu.
"""

h, m, k = map(int, input().split())

k %= 784 #xử lí số phút thêm nếu vượt quá 784 phút
x = h * 28 + m + k #tổng số phút hiện tại và số phút thêm
x %= 784 #tổng số phút có thể lớn hơn 784(sang ngày hôm sau)
h = x // 28
m = x % 28

print(h, m)