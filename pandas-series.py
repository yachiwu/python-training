#載入pandas模組
import pandas as pd
#資料索引
# data = pd.Series([2,3,-5,6,80,10],index = ["a","b","c","d","e","f"])
# print(data)
#觀察資料
# print("資料型態",data.dtype)
# print("資料索引",data.index)
# print("資料大小",data.size)
#取得資料:1.根據順序 2.根據索引
# print("根據順序",data[2])
# print("根據索引",data["f"])
#數字運匴:基本、統計、順序
# print("最大值",data.max())
# print("總和",data.sum())
# print("中位數",data.median())
# print("標準差",data.std())
# print("最大的三個數",data.nlargest(3))
# print("最小的二個數",data.nsmallest(2))

#字串運算:基本、串接、搜尋、取代
data = pd.Series(["你好","Pandas","Python"])

# print("字串全部變小寫",data.str.lower())
# print("字串長度",data.str.len())
# print("把字串串起來，自訂sep(串接的符號)",data.str.cat(sep="-"))
# print("判斷字串有無包含P",data.str.contains("P"))
print("字串取代",data.str.replace("你好", "hello"))
