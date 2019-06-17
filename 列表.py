向列表末尾添加新元素  返回值None
append()
list1 = [1,2,3,4]
print(list1.append(6))
>>>[1,2,3,4,6]

复制列表
copy()
list1 = [1,2,3]
list2 = list1.cope()
print(list2)
>>>[1,2,3]   #list1与list2id不同不指向同一内存

计算某个元素列表中出现的次数
count()
list1 = [1,2,3,4,5,1,1]
print(list1.count(1))
>>>3

每一个列表继承另一个列表
extend()
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1.extend(list2)  此处不赋值给list3 返回值None
print(list1)  
print(list2)
print(list3)
print(list1+list2)
>>>[1,2,3,4,5,6,7,8,9,10]
>>>[6,7,8,9,10]
>>>None
>>>[1,2,3,4,5,6,7,8,9,10,6,7,8,9,10]

获取值在列表中的索引
index()
list1 = [1,3,3,4,5,3,7,8,3,10]
print(list1.index(3))
print(list1.index(3,2,5))  2是开始检索的下标5是结束的下标左包括右不包括
>>>1
>>>2

在指定位置钱插入元素  2个参数
insert()
list1 = [1,2,3,4,5]
list1.insert(2,9)
print(list1)
>>>[1,2,9,3,4,5]

根据索引移除列表内一个元素，不给索引默认移除最后一个 返回移除的那个值
list1 = [1,2,3,4,5]
print(list1.pop(2))
print(list1)
print(list1.pop())
print(list1)
>>>2
>>>[1,3,4,5]
>>>5
>>>[1,3,4]
#当列表没有元素时pop该列表会报错

移除列表中指定的值  返回None
remove()
list1 = ['a','b','c','d']
print(list1.remove('b'))
print(list1)
>>>None
>>>['a','c','d']

列表反转
reverse()
list1 = [1,2,3,4]
list1.reverse()
print(list1)
>>>[4,3,2,1]
list1 id不发生改变

排序 默认从小到大
sort()
list1 = [5,8,6,4,3,7,9,2,1]
print(list1.sort())
>>>[1,2,3,4,5,6,7,8,9]
从大到小
list1.sort(reverse=True)
print(list1)
>>>[9,8,7,6,5,4,3,2,1]
     id不发生改变



