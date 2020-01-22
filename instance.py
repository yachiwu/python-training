#Point實體物件的設計:平面座標上的點
# class  Point:
#     def __init__(self):
#         self.x = 3
#         self.y = 4
# p1 = Point() #建立實體物件
# print(p1.x,p1.y)
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p1 = Point(1,5)
# print(p1.x,p1.y)
# p2 =Point(2,6)
# print(p2.x,p2.y)

#FullName 實體物件的設計:分開紀錄姓、名資料的全名
#定義類別
class FullName:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
#產生實體物件
name1 = FullName("ya-chi","wu")
print(name1.firstname,name1.lastname)        
name2 = FullName("ting-yi","lin")
print(name2.firstname,name2.lastname)      