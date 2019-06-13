笔记
#print()函数的格式化：
print("转换后的温度是{:.2f}C".format(C))
{}表示槽，后续变量填充到槽中
{:.2f}表示将变量C填充到这个位置是取小数点后两位

eval() 去掉参数最外侧引号并执行余下语句的函数 评估函数

>>>eval("1")
1
>>>eval("1+2")
3
>>>eval('"1+2"')
'1+2'
>>>eval('print("hello")')
hello 


turtle库的使用#海龟库是turle绘图体系的python实现
绝对坐标(0,0)
绝对角度
turtle.seth(angle)
seth()改变海龟行进方向
seth()只改变方向但不行进
angle为绝对度数

turtle.left(angle)#向左
turtle.right(angle)#向右
turtle.colormode(mode)#颜色

整数 浮点数 复数 
round(x,d):对x四舍五入，d是小数截取位数
运算 比较浮点数是使用round()函数
浮点数科学计数法表示：<a>e<b>，表示a*10的b次方
例：4.3e-3  为0.0043
复数
z.real 实部
z.imag 虚部
数值运算
+-*/     x/y 浮点数结果 //整数除  +x表示x本身 x%y 余数，
模运算10%3结果是1
x**y 表示幂运算，x的y次幂  与 pow(x,y)一致
当y是小数时，开放运算10**0.5结果是根号10

二元操作符有对应的增强赋值操作符

x op= y ：op为二元操作符
x+=y  x-=y  x*=y  x/=y  x//=y  x%=y  x**=y
>>>x=3.1415
>>>x**=3 # 与x=x**3等价 
31.006276662836743 
功能函数
abs(x) #x的绝对值
divmod(x,y)#商余 输出商和余数
pow(x,y[,z])#幂余，(x**y)%z,[...]表示参数z可省略
round(x[,d])#四舍五入 d表示保留小数位数默认值为0
max(X1,...Xn)#取最大值 n不限
min(X1,...Xn)#取最小值 n不限
数字类型转换函数
int(x)将x变成整数，舍弃小数部分
float(x)将x变成浮点数，增加小数部分
complex(x) 讲x变成复数，正价函数部分 complex(4)结果为4+0j

字符操作
len(x) #长度
str(x)# 转换成字符串 增加引号
eval(x)#去除引号  用于提取用户输入eval(input())   
hex(x)  十六进制 oct(x) 八进制 #小写形式字符串
chr(u) u为Unicode编码，返回其对应的字符
ord(x) x为字符，返回其对应的Unicode编码
Unicode编码 #python字符串的编码方式 统一字符编码 
str.lower()将字符串全部字符小写
str.upper()将字符串全部字符大写
str.split(sep=None) 返回一个列表 ，由str根据sep被分割的部分组成
str.count(sub)返回子串在str中出现的次数
str.replace(old,new)返回子串在str副本，所有old子串被替换为new
str.center(width[fillchar])字符串str根据宽度width居中，fillchar可选 "python".center(20,"=")输出为========python========
str.strip(chars)从str中去除掉在其左侧和右侧chars中列出的字符"=python=".strip("=np")结果为"ytho"
str.join(iter)在iter变量除最后元素外每个元素后添加一个str",".join("12345")结果为"1,2,3,4,5"#主要用于字符串分割等
.format 
time库的使用
time()获取计算机内部时间值   浮点数
ctime()返回字符串   时分秒
gmtime()  表示计算机可处理的时间格式
strftinme() 时间格式化的方法  tpl是格式化模板字符串，用来定义输出效果 ts是计算机内部时间类型变量
>>>t=time.gmtime()
>>>time.strftime("%Y-%m-%d %H:%M:%S",t)#格式化字符串: %Y %m %B %b %d 
'2018-01-26 12:55:20'
strptinme(str，tpl) 用字符串获取时间变量格式 
程序计时
perf_counter()  返回一个cup级别的精确时间区间 结束-开始的差值
sleep(s) s拟休眠的时间  单位秒  可以是浮点数
def wait():
	time.sleep(3.3)
>>>wait() #程序将等待3.3秒后再退出

random库
import random
random.seed(10)  种子
random.random()  0-1间的小数
random(a,b) 生成[a,b]之前的整数
randrange(m,n[,k])生成一个[m,n]之间以k为步长的随机整数
getrandbits(k) 生成一个k比特长的随机整数
uniform(a,b)生成一个[a,b]之前的随机小数 取值范围为小数点后16位
choice(seq) 从序列seq中随机选取一个元素
shuffle(seq)将序列seq中元素随机排列，返回打乱后的序列

函数
可选参数传递
可变参数传递
global 保留字 函数中使用声明为全局变量   函数可处理全局变量
局部变量与全局变量  在函数中局部变量运算之后被释放 
lambda 函数 
#<函数名>lambda < 参数>： <表达式> 用作特定函数或方法的参数
>>>f=lambda x,y:x+y
>>>f(10,15)
25
函数的参数传递
可选参数必须在非可选参数的后面
def 函数名():
def 函数名(非可选参数，可选参数)
设计可变数量参数不确定参数数量 *b可变参数 	
名称参数传递  位置参数传递
递归
def rvs(s):
	if s=="":
		return s
	else:
		return rvs(s[1:])+s[0]
pyinstaller 三方库
-h 查看帮助
--clean 清理打包过程中的临时文件
-d--onedir 默认值，生成dist文件夹
-F--oneflle 在dist文件夹中只生成独立的打包文件
-i<图标文件名.ico>指定打包程序使用的图标(icon)文件
使用举例
pyinstaller-i 图标文件名.icoF 文件名.py

科赫曲线
递归方法 基例

组合数据类型
set 建立空集合  与字典不同  字典直接用{}生成空字典
集合 {}  每个元素唯一，不存在相同元素  集合元素之前无序
集合操作符  S丨T 合集 S，T所有元素   S-T 差集  S减去S和T共同元素  S&T 交集 S和T的共同部分 S^T 补集 ST所有元素减去S和T的共同部分
S<=T 或 S<T S>=T 或S>T
S.add(x) 将x增加到s
S.discard(x)移除S中元素x，如果不在集合S中，不报错
S.remove(x)移除S中元素x，如果x不在集合S中，产生KeyError异常
S.clear()移除S中所有元素
S.pop()随机返回S的一个元素，更新S，若S为空产生KeyError异常
S.copy()返回集合S的一个副本
len(S)返回集合S的元素的个数
x in S 判断S中元素x,x在集合S中，返回True，否则返回False
x not in S 判断S中元素x，x不在集合S中返回True.......
set(x) 将其他类型变量x转变为集合类型
集合类型应用场景
1.数据去重 set 2.包含关系比较
序列类型及操作
元素类型可以不同  具有先后关系的一组元素

操作符及运用
x in s 如果x是序列s元素，返回True，否则返回False
x not in s 如果x是序列s的元素，返回False，否则返回True
s + t 连接两个序列s和t
s*n n*s 将序列s复制n次
s[i] 索引，返回s中的第i个元素，i是序列的序号
s[i:j]或s[i:j::k] 切片，返回序列s中第i到j以k为步长的元素子序列
s.index(x) 或s.index(x,i,j) 返回序列s从i开始到j位置中第一次出现元素x的位置
s.count(x) 返回x在序列s中出现x的总次数

元组
是一种序列类型的扩展 #使用小括号() tuple()创建， 元素间用逗号，分割
可以使用或不使用小括号
def func():
	return 1,2
元组 元素有序排列 元素不可改变 继承序列类型的全部操作
 
 列表
 一种序列类型的扩展 
列表可修改 #使用方括号[] 或list()创建，元素间用逗号，分隔
列表中各元素类型可以不同，无长度限制
ls[i]=x 替换列表ls第i元素为x
ls[i:j:k]=lt 用列表替换ls切片后所对应元素子列表
del ls[i] 删除列表ls中第i元素
del ls [i:j:k]删除列表ls中第i到j以k为步长的元素
ls+=lt 更新列表ls，将列表lt元素增加到列表ls中
ls*=n 更新列表ls，其元素重复n次
ls.append() 增加元素
ls.clear() 删除列表ls中所有元素
ls.copy() 生成一个新列表
ls.insert(i,x) 在第i位置增加x元素
ls.pop(i) 取出i位置元素并删除
ls.remove(x为字符)将列表ls出现的第一个元素x删除
ls.reverse() 将列表ls中的元素反转
tuple(ls) 将列表ls转换成元组类型
基本统计值
sorted()  可以对列表进行排序

字典类型定义 {} dict()创建
映射是一种键（索引）和值（数据）的对应
{<键>:<值>}键值对
type(de) 返回变量de的类型
del d[k] 删除字典d中键k对应的数据值
k in d 判断键k 是否在字典d中，如果在返回True，否则False
d.keys() 返回字典d中所有的键信息
d.valuse() 返回字典d中所有的值信息
d.items()返回字典d中所有的键值对信息
d.get(k,<default>) 键k存在，则返回对应值，不在则返回<default>值
d.pop(k,<default>) 键k存在，则取出相应值，不在则返回<default>值
d.popitem() 随机从字典d中取出一个键值对，以元组形式返回
d.clear()删除所有的键值对
len(d)返回字典d中元素的个数
向字典增加键值对元素 d["a"]=1; d["b"]=2
修改d["b"]=3

字典类型的应用场景

jieba库   #优秀的中文分词第三方库
安装 cmd pip install jieba
三种模式 精确模式、全模式、搜索引擎模式
精确模式：把文本精确的切分开，不存在冗余单词
全模式：把文本所有可能的词语都扫描出来，有冗余
搜索引擎模式：在精确模式基础上，对长词再次切分
jieba.lcut(s) 返回一个列表类型的分词结果
jieba.luct(s,cut_all=True) 全局模式，返回一个列表类型的分词结果，存在冗余
jieba.lcut_for_search(s) 搜索引擎模式，返回一个列表类型的分词结果，存在冗余
jieba.add_word(w):向分词词典增加新词w

def getText():
	txt = open("hamlet,text","r")
	txt = txt.lower()
	for ch in '!"#$%&()+,-./:;<+>@[\\]^_‘{|}~':
		txt = txt.replace(ch,"")
	return txt

hamleTxt=getText()
words = hamleTxt.split
counts=={}
for word in words
	counts[word]=counts.get(word,0)+1
items =list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10)
	word ,count =items[i]
	print("{0:<10}{1:>5}".format(word,count))

文件的打开关闭
步骤：打开-操作-关闭
a=open(<路径及文件名同目录可省路径>,<打开模式> )  打开
C:/PY/f.txt "C:\\PY\\f.txt"  f.txt
打开模式
'r'  只读模式 如果文件不存在  返回FileNotFounfError
'w'  覆盖写模式 文件不存在则创建，存在则完全覆盖
'x'  创建写模式，文件不存在则创建，存在则返回FileExistsError
'a'  追加写模式，文件不存在则创建，存在则在文件最后追加内容
'b'  二进制文件模式
't'  文本模式 默认值
'+'  与r/w/x/a一同使用，在原功能基础上增加同时读写功能
'wb' 二进制形式，覆盖写模式
a.close 关闭
a.read(size)   读入全部内容  size 参数 （长度）
a.readline(size) 读入一行内容 size 参数 该行前size长度
a.readlines(hint)  读入文件所有行，以每行为元素形成列表 如果给出参数读入钱hint行
#读文件
a.write(s) 向文件写入一个字符串或字节流
a.writelines(lines) 将一个元素全为字符串的列表写入文件
a.seek(offset) 改变当前文件操作指针的位置，offset含义如下
0-文件开头；1-当前位置；2-文件结尾
#写文件

一维数据的格式化
由对等关系的 有序 (列表) 或 无序 (集合)数据构成，采用线性方法组织
存储方式一：空格分隔
存储方式二：逗号分隔
存储方式三：其他方式分隔
缺点：数据中不能有英文逗号

二维数据
由多个一维数据构成，是一维数据的组合形式 表格 

多维数据
由一维或二维数据在新维度上扩展形成

高维数据
仅利用最基本的二元关系展示数据间的复杂结构
键值对

数据的操作周期

存储<-> 表示<->操作
数据存储 数据表示


wordcloud库

w.generate(txt)  向WordCloud对象w中加载文本txt
w.to_file(filename) 将词云输出为图像文件，.png，jpg

import wordcloud
c=wordcloud.WordCloud()
c=generate("wordcloud by python")
c.to_file("pywordclound.png")
width 宽
height 高
min_font_size  最小字号 默认4号
max_font_size  最大字号
font_step 字号间隔 默认1
font_path 字体文件的路径  默认None 指定字体
max_words 最大词云显示的最大单词数量 默认200
stop_words 指定词云的排除词列表，即不显示的单词列表
mask 指定词云形状，默认为长方形，需要引用imread()函数
from scipy.misc import imrerd
mk=imread("pic.png")
w=wordcloud.WordCloud(mask=mk)
backgorund_color  图片背景颜色 
https//pypi  python社区
集成安装 Anaconda 

os库
os.path.abspath(A)子库  路径操作   返回A绝对路径
os.path.normpath(A)  #统一用\\分隔路径  归一化A的表示形式
os.path.normpath("d://pye//file.txt")  返回#d:\\pye\\file.txt
os.path.relpath(A)  返回当前程序与文件之间的相对路径(relative path)
os.path.relpath("d://pye//file.txt") 
'..\\..\\..\\..\\..\\..\\..\\pye\\file.txt'
os.path.dimame(path)  返回path中的目录名称（d://pye//file.txt）
'//pye'
os.path.basename(path)  返回path中最后的文件名称
d://pye//file.txt   >>file.txt
os.path.join(path,*paths)  组合path与paths，返回一个路径字符串
>>>os.path.join("d:","/pye/file.txt")
'd:/pye/file.txt'
os.path.exists(path)  判断path对应文件或目录是否存在，返回True或False
os.path.isfile(path)  判断path所对应是否为已存在的文件，返回True或False
os.path.isdir(path)  判断path所对应是否已存在的目录，返回True或False
os.path.getatime()   返回对应文件或目录上一次访问时间
os.path.getmtime()    返回对应文件或目录最近一次修改时间
os.path.getctime()    返回对应文件或目录的创建时间
os.path.getsize()    返回对应文件的大小，以字节为单位

os库之进程管理
import os
os.system(程序路径/及参数)
环境参数
os.chdir(path) 修改当前程序操作的路径  
os.getcwd()    返回程序的当前路径
os.gerlogin()   获取当前系统登录用户信息
os.cpu_count()   获取当前系统的cpu数量
os.urandom(n)   获得n个字节长度的随机字符串，通常用于加解密运算

Numpy  接口使用 
Pandas  数据分析高层次应用库
sciPy   数学、科学和工程计算功能库

Matplotlib 高质量的二维数据可视化功能库
Seaborn 统计类数据可视化功能库
Mayavi 三维科学数据可视化功能库

PyPDF2 用来处理pdf文件的工具集  文本处理
NLTK  自然语言文本处理第三方库
Python-docx 创建或更新 word文件的第三方库

Sclkit-learn 机器学习方法工具集
TensorFlow AlphaGo背后机器学习计算框架
MXNet 基于神经网络的深度学习计算框架



网络web信息爬取
Requests 最友好的网路爬虫功能库
Scrapy  phthon 数据分析高层次应用库
pyspider 强大的web页面爬取系统
Beautiful Soup Html 与xml的解析库
Re  正则表达式解析和处理功能库
python-Goose 提取文章类型web页面的功能库


web网站开发
后端框架 Django 最流行的Web应用框架
Pyramid 规模适中的Web 应用框架
Flask web 应用开发微框架 
WeRoBot 微信公众号开发框架
aip 百度AI开放平台接口
MyQR 二维码生成第三方库

python库之图形用户界面
PyQt5 Qt开发框架的Python接口 扩平台桌面应用开发系统 完备GUI
wxPython 跨平台GUI开发框架
pyGObject 使用GTK+开发GUI的功能库
游戏开发
pyGAME 简单的游戏开发功能库
panda3D 开源、跨平台的3D渲染和游戏开发库 C++ python
cocos2d 构建2d游戏和图形界面交互式应用的框架
VR Zero 在输煤派上开发VR应用的python库
pyovr oculus Rift的python开发接口
Vizard 基于python的通用VR开发引擎
图形艺术
Quads  迭代的艺术
ascii_art  ASCII艺术库
turtle 海龟库是turle绘图体系的python实现

Django
创建项目 命令符 django-admin startproject myblog

runserver 更改地址
wsigi 接口文件  python服务器网关接口 python应用与web服务器之间的接口
startapp 创建应用
migrantions 数据移植(迁移)模块 内容自动生成
admin.py 应用后台管理系统配置
apps.py 应用配置
models.py 数据模块 使用ORM框架 类似于MVC结构中的Models（模型）
tests.py 自动化测试模块
views.py 执行响应的代码所在模块  代码逻辑处理的主要地点




  

















