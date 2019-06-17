a = set()
print(a)
list1 = [1,2,3]
a = set(list1)
print(a)
>>>set()
>>>{1,2,3,4}

向集合中添加元素
set1 = {5,1,4,8,'c','s'}
set1.add(6)
print(set1)
>>>{1,4,5,6,8,'c','s'}

clear() 清空集合
copy()  复制集合
pop()  随机弹出一个元素
a = {'a','b','c',4}
a.pop()    
print(a)
>>>{'b','c''4'}  注意此时不是移除最后一个元素 随机弹出

remove()  删除集合中某个值，如果这个值不在集合中会报错
a = {'a','b','c',4}
a.remove(4)
print(a)
a.remove(4)------会报错
>>>{'a','b','c'}
>>>KeyError

discard()  删除集合中某个值，如果这个值不在集合中什么也不做  返回集合
a = {'a','b','c',4}
a.discard(4)
print(a)
a.discard(4)
print(a)
>>>{'a','b','c'}
>>>{'a','b','c'} # 与remove的区别  值不在时一个会报错一个不会

difference()  差集
difference_update()   区别是第一个返回一个新的集合，第二个是把原来的集合覆盖
set1 = {1,2,3,4,7}
set2 = {2,4,8,11,24}
set3 = set1.difference(set2)
print(set3)
print(set1)
>>>{1,3,7}
>>>{1,2,3,4,7}
difference_update()
set1 = {1,2,3,4,7}
set2 = {2,4,8,11,24}
set3 = set1.difference_update(set2)
print(set3)
print(set1)
>>>None
>>>{1,3,7}
