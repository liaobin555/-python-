清除整个字典 返回None
clear()
dict1 = {'a':1 'b':2 'c':3}
dict1.clear()
print(dict1)
>>>{}

copy()
复制字典
dict1 = {'a':1 'b':2 'c':3}
dict2 = dict1.copy()
print(dict2)
>>>{'a':1 'b':2 'c':3}



按照指定的序列为键创建字典，值都是一样的
fromkeys()
list1 = ['a','b','c']
dict1 = {}.fromkeys(list1)
dict2 = {}.fromkeys(list1,3)
print(dict1,dict2)
>>>{'a':None,'b':None,'c':None}
>>>{'a':3,'b':3,'c':3}

根据键获取指定的值 找不到的键如果没默认值则返回默认值 如果没默认值则返回None
dict1 = {'a':1,'b':1,'c':1}
print(dict1.get('b'))
print(dict1.get('d'))
print(dict1.get('d',4))   ‘4’为当查找键不存在是设定返回的值
>>>2
>>>None
>>>4

将字典变成类似于元组的形式方便遍历
itesm()
dict1 = {'a':1,'b':2,'c':3}
for k,v in dict1 itesm():
	print(k,v)
for i in dict1.itesm():
	print(i)
print(dict1.itesm())
>>>
a 1
b 2
c 3
('a',1)
('b',2)
('c',3)
dict_items([('a',1),('b',2),('c',3)])

移除字典中指定元素 返回键所对应的值，
如果键不存在，则返回默认值，如果键找不到没有默认值时会报错
pop()
dict1 = {'a':1,'b':2,'c':3}
print(dict1.pop('a'))
print(dict1)
print(dict1.pop('d',4)) 字典中没有键'd'  指定默认4返回
print(dict1.pop('d'))   字典中没有键'd'  不给定默认值会报错
>>>1
>>>{'b':2,'c':3}
>>>4
>>>报错

移除字典的键值对 返回移除的键和值  不指定
popitem()
dict1 = {'a':1,'b':2,'c':3}
print(dict1.popitem())   不指定默认移除最后一个元素
>>>('c',3) 

在字典添加一个元素  如果有这个键存在则返回他的值
setdefault()
dict1 = {'a':1,'b':2,'c':3}
print(dict1.setdefault('d',5))
print(dict1)
>>>5
>>>{'a':1,'b':2,'c':3,'d':5}

修改字典中的值
uodate()
dict1 = {'a':1,'b':2,'c':3}
dict1.update({'a':5,'b':4})
print(dict1)
>>>{'a':5,'b':4,'c':3}





