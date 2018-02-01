# ---------------------
# H01 註解
#### 先改成marksown,#越多，字體越小
print("Hello World")
#### \跳脫字元
print("Jim's apple")
print('Jim\'s apple')   # \' 跳脫字元

# ---------------------
# H02 變數
#### python變數不須事先定義
#### 命名規則 "a-z","A-z","_" 且不可為系統保留字
a = "Hello"
print(a)
a = 1.2
print(a)
#### 字串 跟+(沒空格),(有空格)相連
a = "Hello"
b = "World"
print(a, b)
print(a + b)
a, b = "Yo", "Check it out"
print(a, b)
print(a + b)

# ---------------------
# H03 Input
#### input() 會回傳輸入的字串
#age = input("請問你今年貴庚") 暫時註解############
age = 0
print(age)
#### 查詢變數的型態 type()
print(type(age))

# ---------------------
# H04 String not list
S = "Jim's apple pen"
print(S)
#### 0開始
#### :包頭不包尾
print(type(S))
print(S[0:2])
#### 負數當作倒數
#### 頭尾都可以開放
print(S[-5:-1])
#### 長度 len()
print(len(S))
#### 沒數字代表開放(最前面/最後面)
print(S[:])

# ---------------------
# H05 Vairables
A = 3       #int
B = 1.234   #float
C = True    #bool
D = "ok"    #str
print(A + C)
#print(A + D) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#### str()轉成字串
print(str(A) + D)
print(A * D)

# ---------------------
# H06 算術運算式
#### + - ** / % // ***
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(-10/3)
print(10%3)    # %餘數
print(10//3)   # //取高斯符號 不大於該數的最大整數
print(-10//3)
print(10**3)   # 10的3次方

# ---------------------
# H07 關係式
#### < <= > >= == !=
#### 會回傳True False

print(5>4)
print(5==4)
print(5<4)
print(5!=4)

# ---------------------
# H08 邏輯運算式
#### and or not
a = True and True
b = True and False
c = False and False
d = True or True      # or兩個條件其一成立即可
e = True or False
f = False or False
g = not False

#### sep當作間隔
print(a, b, c, d, e, f, g, sep=", ")

# ---------------------
# H09 While
aa = 0
while aa < 3:
    print(aa)
    aa = aa + 1

# ---------------------
# H10 if elif else
x, y, z = 3, 9, 6
if x < y :
    print("x<y")
age = 10
if int(age) >= 18 :
    print("恭喜你可以去看紅衣小女孩2")
else :
    print("太嫩囉~笑你")

# ---------------------
# H11 For
#### for item in sequence:
#### []list
example = [1, 3, "5", "OK", 3.14, True, False]
for i in example :
    print(i*3)

ST = "Test Str"
for i in ST :
    print(i*3)

# ---------------------
# H12 list[]
#### []=> list
#### ()=> tuple(裡面東西不能變)
#### {}=> dic, set
example = [1, 3, "5", "OK", 3.14]

#### [] list
#### 逗點隔開
#### 順序 從0
#### 內容不拘

print(example[:2])
print(example[2:])
#### len() 個數
print(len(example))
print(example[0] + example[-1])

#### in 檢查有沒有在這個list裡面 回傳True False
print(2 in example)
print("OK" in example)

#### 新增
#### append(), insert(index, value), extend()
example.append(8)
example.insert(5,9)
example.extend([10, 11])
print("新增 : " , example)
#### 修改
example[0] = 0
print("修改 : " , example)
#### 刪除 del
del example[0]
print("刪除 : " , example)
del example[0:]
print("刪除全部 : " , example)

#### list string 差別
#### list 可放各樣的東西，也可以放list
#### list 可以新增修改裡面東西
multi_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_1[1])
print(8 in multi_1[2])

# ---------------------
# H13 Tuple()
#### tuple不能修改
t = (1, 2, 3)
l = [1, 3, 3]
print(t)
print(l)

formatA = "%s %s %s"
valuesB = ("6", "8", "good")
print(formatA % valuesB)

formatA = "原來您是%s歲的%s"
age = 30
c = "大法師"
valuesB = (age, c)
print(formatA % valuesB)

# ---------------------
# H14 dic
#### {key1 : value1, key2 : value2}
#### dictionary 就是 key-value pair
#### value可重複，但key值唯一
week = {"Mon":"星期一",
        "Tue":"星期二",
        "Wed":"星期三"}
print(week["Wed"])
print(type(week))

#### keys
print(week.keys())
#### values
print(week.values())
#### items 會用tuple裝
print(week.items())

#### 直接新增
week["Thur"] = "星期四"
print(week)
#### 從空白新增
week01 = {}
week01["Mon"] = "周一"
week01["Fri"] = "周五"
print(week01)
for i in week :
    print(i , " : ", week[i])

####為複雜操作
inventory = {
    "coin" : 50,
    "wallet" : ["Student ID", "Keys"],
    "backpack" : {
        "book" : 2,
        "phone" : 1,
        "NB" : 2
    }
}
print(inventory)
print(inventory["wallet"])
print(inventory["wallet"][0])
print(len(inventory["wallet"]))    # 長度
inventory["wallet"].append("credit card")    # 新增
print(inventory["wallet"])

print(inventory["backpack"])
print(inventory["backpack"]["book"])
print(len(inventory["backpack"]))    # 長度
inventory["backpack"]["earphone"] = 3    # 新增
print(inventory["backpack"])

inventory["coin"] += 50
print(inventory)

#### 合併 update() 消去重複的
#### 合併 week 跟 week01
print(week)
print(week01)

week.update(week01)
print(week)

# ---------------------
# H15 set
#### set=>{} 不能重複
setA = {2, 4, 6}
print(setA)
listA = [1, 2, 1, 4, 3]
print(listA)
#### 重複的去掉
setB = set(listA)
print(setB)
#### 交集 & 共同有的值
print(setB & setA)
#### 聯集 | 全部出現
print(setB | setA)
#### 差集 - 把有交集的刪掉剩下的
print(setB - setA)
print(setA - setB)

# ---------------------
# H16 def the function
####def 一個函式
#### 沒參數
def span() :
    return("呵呵")
print(span())
#### 有參數
def spamm(i="呵"):
    return(i+" 河三小")
print(spamm())          # 沒有給值就是預設值
print(spamm(span()))    # 有給值就用給的值

def iniTest(a="A",b="B"):
    return(a+b)
print(iniTest("C"))     # 覆寫第一個參數
print(iniTest("C",))    # 覆寫第一個參數
# print(iniTest(,"D"))  # error
print(iniTest(b="D"))   # 覆寫第二個參數，第一個用預設值
print(iniTest(b="D", a="C"))    # 不用按照順序給
print(iniTest("C","D")) # 覆寫兩個參數
# print(iniTest(,)) # error
print(iniTest())    # 直接用預設值

# ---------------------
# H17 牛刀小試
dic = {
    "Tom" : 100,
    "Mary" : 95,
    "Gary" : 88,
    "Tim" : 80,
    "Eva" : 95
}
def check_dic(name):    #較精簡
    if name in dic:
        print(name + "\'s score is", dic[name])
    else:
        print(name , "He/She is not in this class")
print(check_dic("Gary"))
print(check_dic("sdf"))

def check_dic01(name):  #較多餘
    for i in dic :
        if i == name :
            print(name + "\'s score is", dic[name])
            break
    else :
        print("He/She is not in this class")
print(check_dic01("Gary"))
print(check_dic01("sdf"))

####轉型
# int() 轉成int
# str() 轉成字串
# set(list) 轉成set