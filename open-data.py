#串接公開資料
import urllib.request as request
import json
src = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=17"  
with request.urlopen(src) as response:
    data = json.load(response)
# print(data)    
#將演唱會資訊印出(名稱)
# for show in data:
#     print("\n",show["title"])
#     for showinfo in show["showInfo"]:
#         print("時間:",showinfo["time"],"地點:",showinfo["locationName"])
#將演唱會資訊寫入show.txt
with open("show.txt","w",encoding="utf-8") as file:
    for show in data:
        file.write(show["title"]+"\n")
        for showinfo in show["showInfo"]:
            file.write("時間:"+showinfo["time"]+" "+"地點:"+showinfo["locationName"]+"\n")
        else:#for迴圈跑到最後一輪時在加一次換行讓show.txt資訊較清楚
            file.write("\n")    