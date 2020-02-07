#載入pandas模組
import pandas as pd
#篩選練習 Series
# data = pd.Series([30,15,20])
# condition = data>18
# print(condition)
# filteredData = data[condition]
# print(filteredData)
# data = pd.Series(["您好","python","pandas"])
# conditon = data.str.contains("p")
# print(conditon)
# filteredData = data[conditon]
# print(filteredData)
#篩選練習 DataFrame
#DataFrame 篩選是針對資料"列"
data = pd.DataFrame({
    "name" : ["Amy","Bob","John"],
    "salary" : [30000,40000,50000]
})
# conditon = data["salary"]>=40000
conditon = data["name"]=="Amy"
print(conditon)
filteredData = data[conditon]
print(filteredData)