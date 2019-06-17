将首字母大写
capitalize()
s = "wang"
print(s.capitalize())
>>>Wang

将每个单词的首字母大写
title() 
s = "wang xiao jing"
print(s.title())
>>>Wang Xiao Jing

将所有字母变为小写字母 
lower()
s = "W"
print(s.lower())
>>>w

将所有字母变为大写字母
upper()
s = "w"
print(s.upper())
>>>W

大小写互换  
swapcase()
s = "w"
print(s.swapcase())
>>>W

返回字符串长度
len()
s = "i love you"
print(len(s))
>>>10

查找指定字符串
find()  找不到返回-1   第一次找的返回第一次索引值
index()  找不到会报错
s = "woord"
s1 = s.find("o",1)  *1为开始检索字符的下标
s2 = s.index("r")
print(s1)
print(s2)
>>>1
>>>3

计算字符串出现计数 返回整形
count()
s = "assssss"
print(count("s"))
>>>6

检测是否以指定字母开头  返回布尔值
endswith()   检查结束
startswith()  检查开始

is判断
isspace()   判断是否为空字符串
islower()   判断是否为小写（所有）
isupper()   判断是否为大写（所有）
istitle()   判断每个单词首字母是否为大写
isalpha()   检测字符串是否是字母组成  返回布尔值
#汉字在英文字符包裹中被当做字符处理（左右都为英文字符时，以汉字开始结束时也为true）
isalnum()   检测字符串是否有字母加数字组成至少有一个字符并且所有字母或数字   返回布尔值
#汉字汉字在英文字符包裹中被当做英文字符处理
isdigit()   
isdecimal()
isnumeric()  
#注意数字判断，详细自我查询

用指定字符切割字符串 返回字符串组成的列表
split()
s = "日照香炉生紫烟*疑是银河落九天"
print(s.split("*"))
>>>['日照香炉生紫烟','疑是银河落九天']  此时返回的是一个列表形式

str.partition(str)
用指定字符切割字符串 返回3元的元组
str = "www.runoob.com"
print str.partition(".")
>>>('www', '.', 'runoob.com')

splitlines()  用换行或者/n切割字符串
s = '''日照香炉生紫烟/n疑是银河落九天
飞流直下三千尺'''
print(s.splitlines())
>>>["日照香炉生紫烟","疑是银河落九天","飞流直下三千尺"]  返回列表

将列表按照指定字符串连接    返回字符串组成的列表
join()
list1 = ["日照香炉生紫烟","疑是银河落九天","飞流直下三千尺"]
s = "*".join(list1)
print(s)
>>>日照香炉生紫烟*疑是银河落九天*飞流直下三千尺

指定字符串的长度，内容靠左边，不足的位置用指定字符填充，默认空格 返回字符串
ljust()
s = 'abc'
print(len(s))
print(s.ljust(5)+'a')
>>>3
>>>abc  a
指定字符串的长度，内容居中，不足的位置用指定字符填充，默认空格
center()
print(s.center(5,"#"))
>>>#abc#
指定字符串的长度，内容靠右，不足的位置用指定字符填充，默认空格
rjust()s = 'abc'
print(len(s))
print(s.ljust(5,"0"))
>>>3
>>>00abc

去掉左右两边指定字符，默认是去掉空格
strip()
lstrip()
rstrip()

s ="  abc"
print('-'+s.strip()+'-')
print('-'+s+'-')
>>>-abc-
>>>-  abc-

指定字符串的长度，内容靠右，不足用位置用0填充
zfill()
s = 'abc'
print(s.zfill(5))
>>>00abc

生成用于字符串替换的映射表
maketrans()
translate()
s = '今天我吃了小桃子，可好吃了'
table = s.maketrans('小桃子'，'大西瓜')   #maketrans  要求字符长度一样
print(table)
print(s.translate(table))  
>>>{23567: 22823, 26691: 35199, 23376: 29916}  #maketrans编码替换
>>>今天我吃了大西瓜，可好吃了#s.translate(table)打印

str.count(sub)返回子串sub在str中出现的次数

str.replace(old,new)返回子串在str副本，所有old子串被替换为new
str.replace(old, new[, max])
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次

str.encode(encoding='UTF-8',errors='strict')
Python encode() 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。

str.endswith(suffix[, start[, end]]) 返回布尔值  用于判断字符串是否以指定后缀结尾
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。

'将字符串中转义字符\t制表符转为空格，默认数为8个'
str.expandtabs()
S = "科目\t语文\t英语\t数学\t体育\n星期一\t星期2\t星期2\t星期2\t星期2"
s = S.expandtabs(8)
print(s)
>>>科目      语文      英语      数学      体育
   星期一     星期2     星期2     星期2     星期2


针对字典的格式化
format_map()
People = {"name": "john", "age": 33}
print("My name is {name},iam{age} old".format_map(People))

# 结果为
# My name is john,iam33 old

检测是否以指定子字符串开头
startswith()
str.startswith(substr, beg=0,end=len(string));
str -- 检测的字符串。
substr -- 指定的子字符串。
strbeg -- 可选参数用于设置字符串检测的起始位置。
strend -- 可选参数用于设置字符串检测的结束位置。
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))   # 字符串是否以 this 开头
print (str.startswith( 'string', 8 ))  # 从第八个字符开始的字符串是否以 string 开头
print (str.startswith( 'this', 2, 4 )) # 从第2个字符开始到第四个字符结束的字符串是否以 this 开头



