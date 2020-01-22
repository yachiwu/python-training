#Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
# p = Point(6,8)
# p.show()#呼叫實體方法/函式
# result = p.distance(0,0)#計算座標(6,8)與原點的距離
# print(result)

#File實體物件的設計:包裝檔案讀取的程式
# class File:
#     def __init__(self,name):
#         self.name = name
#         self.file = None
#     def openfile(self):
#         self.file = open(self.name,mode = "r",encoding="utf-8")   
#     def read(self):
#         return self.file.read()
# #讀取檔案範例
# f1 = File("data1.txt")
# f1.openfile()
# info = f1.read()
# print(info)

class File:
    def __init__(self,name):
        self.name = name
    def open_read_file(self):
        with open(self.name,mode = "r",encoding="utf-8")  as file:
            info = file.read()
            print(info)
f1 = File("data1.txt")
f1.open_read_file()