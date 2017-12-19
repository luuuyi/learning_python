import os

# Python的字典不排序，不能用index下标去取值，猜测相等判断应该使用的是hash
tmp_1 = {1:'ss', 2:'ee'}
tmp_2 = {2:'ee', 1:'ss'}
print tmp_1 == tmp_2      # True

# 使用in判断语句的时候，其实操作的是字典的key
print 1 in tmp_1         #True
print 'ss' in tmp_2      #False

# 将字典类型返回list结果
tmp_2 = {2:'ee', 1:'ss'}
for i in tmp_2.values():
    print i
for i in tmp_2.keys():
    print tmp_2[i]
for k, v in tmp_2.items():
    print k, tmp_2[k]

# Python中get函数和[]比较像，不过在字典中不存在相应的key时提供一个备选值
tmp_2 = {2:'ee', 1:'ss'}
print tmp_2.get(3, 'gg')      # gg
tmp_2.setdefault(3, 'dd')  

