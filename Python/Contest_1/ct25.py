'''
28tech có rất nhiều tiền :v. Anh ta có n đô la trong ngân hàng. Vì lý do bảo mật
    , anh ta muốn rút tiền mặt (chúng tôi sẽ không tiết lộ lý do tại đây). 
Các mệnh giá cho tờ đô la là 1, 5, 10, 20, 100. 
Số tờ tiền tối thiểu mà 28tech có thể nhận được sau khi rút toàn bộ số dư của mình là bao nhiêu?
'''

n = int(input())

num_cash = n // 100

remain_cash = n % 100
num_cash += remain_cash // 20

remain_cash = n % 20
num_cash += remain_cash // 10

remain_cash = n %  10
num_cash += remain_cash // 5

remain_cash = n % 5
num_cash += remain_cash

print(num_cash)