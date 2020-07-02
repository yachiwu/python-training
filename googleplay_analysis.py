import pandas as pd
#讀取資料
data = pd.read_csv("googleplaystore.csv")#把csv檔案讀取成一個DataFrame
#觀察資料
print("資料數量,欄位",data.shape)
print("資料欄位名稱",data.columns)
print("==========================")
#分析資料:評分的各種統計數據
# condition = data["Rating"]<=5
# data = data[condition]
# print(data)
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("取得前一千個應用程式的平均",data["Rating"].nlargest(1000).mean())
#分析資料:安裝的各種統計數據

# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# print("平均數",data["Installs"].mean())
# condition = data["Installs"]>100000
# print("安裝數量大於十萬有幾個?",data[condition].shape[0])
#基於資料的應用:關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字: ")
codition = data["App"].str.contains(keyword,case=False) #忽略大小寫搜尋
print(data[codition]["App"])
print("數量",data[codition]["App"].shape[0])