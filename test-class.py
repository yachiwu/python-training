#定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO，有兩個屬性:supportedSrc,read
class IO:
    supportedSrc = ["concole","file"]
    def read(src):
        if src not in IO.supportedSrc:
            print("not surpport")
        else:
            print("read form",src)
#使用類別
print(IO.supportedSrc)
IO.read("file")    
IO.read("internet") 