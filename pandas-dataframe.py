#載入pandas模組
import pandas as pd
#資料索引 pd.DataFrame(字典,index=索引列表)
data = pd.DataFrame({
    "name": ["Lucy","Amy","Bob","JoJo"],
    "salary" : [30000,40000,45000,20000]

},index = ["a","b","c","d"])
print(data)
print("===================")
#觀察資料
# print("資料數量",data.size)
# print("資料形狀(列,欄):",data.shape)
# print("資料索引",data.index)

#取得列(Row/橫向)的Series資料:根據順序、根據索引
# print("取得第 二 列",data.iloc[1],sep="\n")
# print("===================")
# print("取得第 d 列",data.loc["d"],sep="\n")
#取得欄(Column/直向)的Series資料:根據欄位的名稱
# print("取得 name 欄位",data["name"],sep="\n")

#結合Series運用
# names = data["name"] #取得單維度Series的資料
# print("把names全部轉為大寫",names.str.upper(),sep="\n")

# salaries = data["salary"]
# print("薪水平均值",salaries.mean())

#建立新的欄位
data["revenue"] = [500000,400000,200000,300000] #data["新欄位名稱"] = [列表]
data["rank"] = pd.Series([1,3,2,4],index = ["a","b","c","d"]) #data["新欄位名稱"] = Series資料
data["cp"] = data["revenue"]/data["salary"]
print(data)