'''
Có năm người chơi một trò chơi gọi là "Sự hào phóng". 
Mỗi người đưa ra một số lượng tiền xu khác không b như một lần đặt cược ban đầu. 
Sau khi tất cả người chơi đặt cược tiền xu của họ
    , thao tác sau được lặp lại nhiều lần: một đồng xu được chuyển từ người chơi này sang người chơi khác. 
Nhiệm vụ của bạn là viết một chương trình có thể, với số lượng xu mà mỗi người chơi có vào cuối trò chơi
    , xác định kích thước b của lần đặt cược ban đầu hoặc chỉ ra rằng kết quả của trò chơi không thể đạt được.
'''

c1, c2, c3, c4, c5 = map(int, input().split())

total = c1 + c2 + c3 + c4 + c5

if total % 5 == 0:
    if total != 0:
        print(total // 5)
    else:
        print("-1")
else:
    print("-1")