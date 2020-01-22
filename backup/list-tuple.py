#有序可變動列表list
# grades = [12,60,90,100]
# #連續刪除列表中從編號1到編號3(不包含)的資料
# grades[1:3] = []
# #列表串接
# grades = grades+[30,33,66]
#print(len(grades))
#巢壯列表
# data = [[3,4,5],[6,7,8]]
# print(data[0][1])
#有序不可變動列表 tuple
data = (3,4,5)
print(data[0:2])
#錯誤 tuple不能做資料更動
#data[0] = 5 
print(data)