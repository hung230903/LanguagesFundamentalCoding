#Câu lệnh print:
    # print(object, sep = seperator, end  = end)
        # object: các đối tượng trong python
        # sep: phân cách giữa các đối tượng khi thực hiện câu lệnh
        #        , nếu không có tham số này thì mặc định sẽ là dấu cách
        # end: chỉ ra kí tự được in ở cuối của dòng
        #       , nếu không có tham số này thì mặc định sẽ là kí tự xuống dòng

#object bên trong print có thể đc đặt trong dấu nháy '' đơn hoặc nháy kép ""
print("object bên trong print có thể đc đặt trong dấu nháy '' đơn hoặc nháy kép:")
print('lmao')
print("lmao")
print("---")

#print nhiều object
print("print nhiều object:")
print('adu', 'vjp' , 'pro')
print("---")

#print có tham số sep
print("print có tham số sep:")
print("adu" , "vjp", "hjphop", sep = '--') 
print("adu" , "vjp", "hjphop", sep = '**')
print("---")

#print có tham số end
print("print có tham số end:")
print("adu" , "vjp", "hjphop", end = '!') 
print("\n---")

#print có cả 3 tham số
print("print có cả 3 tham số:")
print("adu" , "vjp", "hjphop",sep = '--', end = '!') 

