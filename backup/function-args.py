#參數的預設資料
# def power(base,exp = 0):
#     print(base**exp)
# power(3,2)    
# power(4)
#使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(n2 = 2,n1 = 4)    
#無限/不定參數資料 #tuple方式
def avg(*numbers):
    print(numbers,"的平均")
    sum = 0
    for n in numbers:
        sum+=n
    print(sum/len(numbers))    
    
avg(3,4)    
avg(5,6,7)
avg(1,-1,-8,6)