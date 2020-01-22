#判斷式
# x =  input("請輸入數字") #取得字串形式的使用者輸入
# x = int(x) #轉換成數字型態
# if x>200:
#     print("大於200")
# elif x>100:
#     print("小於200 大於100")
# else:
#     print("小於等於100")
#四則運算
n1 = int(input("請輸入數字一 : "))
n2 = int(input("請輸入數字二 : "))
op = input("請輸入 +,-,*,/,:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("運算符號輸入錯誤")