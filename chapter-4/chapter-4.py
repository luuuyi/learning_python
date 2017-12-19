import os

# 操作列表
spam = ['cat', 'dog', 'pig', 'horse']
print spam[0]   # 不能使用超过len的下标或者浮点型下标来取值
print spam[-1]   # 不能使用超过len的负数下标，-1表示倒数第一个
print spam[-5]   # 错误的

# 使用list的切片获取子list
print spam[0:4]  # 下标范围为[0, 4)
print spam[3:1]  # 此时返回为一个空的list
print spam[0:-1] # 等价于下标范围为[0, 3)

# list可以组合不同类型的数值，同时列表与字符串一样接受+和*操作符
spam[2] = 111
print spam + [1,2,3]
print spam * 3

# 使用list，统计列表的下标
del spam[2]
for i in range(len(spam)):
    print i, spam[i]

# in和not in语句
test = [1,2,3,4,5,6]
print 1 in test      #True
print 0 not in test  #False

# 多重赋值，适用于def函数的返回，适用于元组和list
test = [1,2,3]
a, b, c = test         # 需要list长度和被赋值的变量数量相当

# list使用index通过值找下标，用[]通过下标找值，还有一些常用的list方法
test = [1,2,3]
print test.index(1)     # 0
print test.append(4)    # [1,2,3,4]
print test.insert(1, 5) # [1,5,2,3,4]
print test.remove(4)    # [1,5,2,3]
print test.sort()
print test.sort(reverse=True)
print test.sort(key=str.lower)   # 使用字典序的排序，不然是ASCII字符顺序排序

# 字符串和元组与list一样，方法大部分也相同，但是字符串和元组的元素不会被改变
name = 'sfddsf'
name[1] = 's'      # 错误
tmp = (1,2,3,4,5)
tmp[1] = 0         # 错误

# 在Python中list()，tuple()，str()可以互相转换，Python中列表使用的是浅拷贝等引用手段
print str([1,2,3,4])     #'[1,2,3,4]'
print list('str')        #['s', 't', 'r']
tmp = [1,2,3,4]
x   = tmp
x.append(5)
print tmp                #[1,2,3,4,5]

# copy模块可以实现深拷贝，copy()和deepcopy()函数
import copy
tmp_1 = [1,2,3]
tmp_2 = copy.copy(tmp_1)

tmp_1 = [1,2,3,[1,2,3]]
tmp_2 = copy.deepcopy(tmp_1)