#修改成可以一次抓取好幾頁的資料 
#利用函式重複執行
def getdata(url):
    #抓取PTT電影版網頁原始碼
    import urllib.request as req
    #建立一個Request物件附加Request headers 的資訊
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    #解析原始碼取得每篇文章標題
    import bs4
    root = bs4.BeautifulSoup(data,"html.parser")#用BeautifulSoup解析html
    titles = root.find_all("div",class_= "title")#尋找所有class = "title"的div標籤
    # print(root.title.string)
    # print(titles)
    for title in titles:  #每次抓取一個標題
        if title.a != None: #如果標籤中包含a標籤(也就是說沒有被刪除的標題)則印出來
            print(title.a.string)
    #抓取道上一頁的超連結
    nextlink = root.find("a",string="‹ 上頁")
    return nextlink["href"]

#主程式執行
pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
#可以重複抓取五次
while count<5:
    pageurl = "https://www.ptt.cc"+getdata(pageurl)
    count+=1
    print("第",count+1,"頁")
