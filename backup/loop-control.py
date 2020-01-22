#break範例
# n = 0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("結束的n:",n)
#continue範例
# n = 0
# for x in [0,1,2,3]:
#     if x%2==0:#x可以被2整除
#         continue
#     print(x)
#     n+=1
# print("最後的n",n)    
#else 簡易範例
# sum = 0
# for i in range(11):
#     sum+=i
# else:
#     print(sum)    #印出1+2+3..+10
#綜合範例 整數平方根
#輸入9 得到3
#輸入11 得到"沒有整數平方根"
n = int(input("請輸入數字"))
# for i in range(n):#i從0~n-1
#     if i*i == n:
#         print("整數平方根,平方根等於", i)
#         break
#     elif i==n-1:
#         print("no")
       
        

# else:
#     print("沒有得到整數平方根")    
i = 0
while i<n:
    if i*i ==n:
        print(n,"的平方根",i)
        break
    else:
        i+=1    
else:
    print("no")         