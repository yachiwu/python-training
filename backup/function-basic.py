#定義函式
# def multiply(n1,n2):
#     value = n1*n2
#     return value
# 呼叫函式
# value = multiply(3,4)+multiply(4,5)
# print(value)

#函式可以用來做程式的包裝，同樣的邏輯可以重複利用
#從1+2+...+n的和
def calculate(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum    
print(calculate(10))
print(calculate(20))