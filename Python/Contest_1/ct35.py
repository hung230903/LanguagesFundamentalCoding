'''
Năm mới sắp đến và bạn rất hào hứng muốn biết còn lại bao nhiêu phút trước Tết. 
Bạn biết rằng hiện tại đồng hồ hiển thị h giờ và m phút
    , trong đó 0≤hh <24 và 0≤mm <60. Chúng tôi sử dụng định dạng thời gian 24 giờ! 
Nhiệm vụ của bạn là tìm số phút trước Tết. Bạn biết rằng năm mới đến khi đồng hồ hiển thị 0 giờ và 0 phút.
'''

h, m = map(int, input().split())

minute = 1440

print(1440 - (h*60 + m))
