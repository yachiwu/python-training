#載入pandas模組
import pandas as pd
#建立Series
data = pd.Series([10,30,20])
#基本Series操作
# print(data)
# print("max",data.max())
# print("median",data.median())
# data = data*2
# print(data)

#比較運算
# data = data==20
# print(data)


#建立DataFrame
# pd.DataFrame(字典)
data = pd.DataFrame({
    "name" : ["lucy","john","nina"],
    "salary" : [3000,2000,5000]
})
#基本DataFrame操作
# print(data)
#取得特定欄位
# print(data["salary"])
#取得特定列
print(data)
print("-------------印特定欄------------")
print(data["salary"])
print("-------------印特定列------------")
print(data.iloc[1])
