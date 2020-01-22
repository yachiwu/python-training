#隨機模組
# import random
#隨機選取
# data = random.choice([1,2,3,4,5])
# print(data)
# data = random.sample([1,2,3,4,5],3)
# print(data)
#隨機調換順序(洗牌)
# data = [1,5,8,10,20]
# random.shuffle(data)
# print(data)
#隨機取得亂數
# data = random.random()#取得0~1之間的隨機亂數
#等同於
# data = random.uniform(0.0,1.0)
# print(data)
#取得常態分配亂數
#平均數100，標準差10，得到的資料多數在90~110之間
# data = random.normalvariate(100,10)
# print(data)
#統計模組
import statistics as stat
#取得平均數
# data = stat.mean([1,4,5,8])
#取得中位數
# data = stat.median([1,4,5,8])
#取得標準差
data = stat.stdev([1,4,5,8,10])
print(data)