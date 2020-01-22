#儲存檔案
# file1 = open("data.txt",mode = "w",encoding="utf-8")#開啟
# file1.write("hello\n第二行")#操作
# file1.close()#關閉
#最佳實務
# with open("data.txt",mode = "w",encoding ="utf-8") as file1:
#     file1.write("測試最佳實務")
#讀取檔案
#把檔案中數字一行一行讀出，計算總合
# sum = 0
# with open("data.txt",mode = "r",encoding="utf-8") as file1:
#     for line in file1:#一行一行讀
#         sum+=int(line)
#     print(sum)
#使用json格式讀取、複寫檔案
import json
#從檔案中讀取json資料放入變數data中
with open("config.json",mode = "r") as file1:
    data = json.load(file1)
print(data)#字典格式
# print(data["name"])    
# print(data["version"])
data["name"]= "112name"#修改變數中的資料
#更新資料回檔案
with open("config.json",mode = "w") as file1:
    json.dump(data,file1)