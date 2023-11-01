#　HomeWork#1 from  01057133張晉源HW#1.py

# 定義 List
list = [12, 60, 15, 70, 90]

# 1. 顯示 List 的內容與長度
print(list,"的長度為:",len(list))

# 2. 刪除[15,70]並顯示 List 內容
list.remove(15)
list.remove(70)
print("刪除[15,70] ==>",list)

# 3. 串接[12,33]並顯示 List 內容
list.extend([12, 33])
print("串接[12,33] ==>",list)

# 4. 置換[60,90]為[5,5,5]並顯示 List 內容
list[list.index(60)] = list[list.index(90)] = 5
list.insert(2,5)
print("置換[60,90]為[5,5,5] ==>",list)

# 5. 顯示 Tuple=(3, 4, 5) 資料及其長度
tuple = (3, 4, 5)
print(tuple,"的長度為:",len(tuple))

# 6. 串接(6,7) 後之內容及其長度
tuple += (6, 7)
print("串接(6,7) ==>",tuple,"長度為:",len(tuple))

# 7. 兩集合 s1 和 s2
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 列印交集和聯集
intersection = s1.intersection(s2)
union = s1.union(s2)
print("兩集合之交集為:",intersection)
print("兩集合之聯集為:",union)

# 8. 某集合運算使其僅保留 "NTOU"
set = {"NTOU", "MMD"}
set.intersection_update({"NTOU"})
print(set)

# 9. 字典 {"NTOU":"國立臺灣海洋大學 ", "MMD":"商船學系", "CSE":"資工系"}
dict = {"NTOU": "國立臺灣海洋大學", "MMD": "商船學系", "CSE": "資工系"}

# 顯示 "我系名稱"
print(dict["NTOU"],dict["CSE"])

# 10. 某字典為2～9的平方，並印出其結果於一串列

dict1={x:x*x for x in [2,3,4,5,6,7,8,9,]}
print(dict1)