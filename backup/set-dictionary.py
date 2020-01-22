#集合
# s1 = {3,4,5}
# s2 = {4,5,6,7}
#交集:取兩個集合中相同的資料
# s3 = s1&s2
#聯集:取兩個集合中所有資料，但不重複取
#s3 = s1|s2 
#差集:從s1中減去和s2重疊的部分
#s3 = s1-s2
#反交集 :取兩個集合中，不重疊的部分
#s3 = s1^s2
#print(10 not in s1)
# print(s3)
#把字串中的字母拆解成集合
# s = set("hello") 
# print("h" in s)
#字典的運算 key-value 配對
# dic = {"apple":"蘋果","bug":"蟲"}
# print(dic["apple"])
# dic = {"apple":"蘋果","bug":"蟲"}
# print( "apple" in dic) #判斷key是否存在字典
# dic = {"apple":"蘋果","bug":"蟲"}
# print(dic)
# del dic["apple"] #刪除字典中的鍵值對
# print(dic)
#從列表的資料產生字典
dic1 ={i:i*3 for i in [1,2,3]}
print(dic1)