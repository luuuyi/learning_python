import os

#操作符，返回的bool值和C++不一样
print False, True
print 'Hell0' == 'hello' # False

#bool值操作符，区别于C++的&&和||这类符号
print True and False, True or False # false, true
print not True # false

#if条件语句
a = 1
if a == 1:
    print True
else:
    print False

if a == 1:
    print True
elif a == 2:
    print True
else:
    print False

#while循环语句
a = 1
while a < 5:
    a = a + 1
    if a == 4:
        break #or continue

#for, range()搭配使用
for i in range(10):
    print i # 0~9

range(12, 17) #[12, 17)
range(0, 10, 2) #[0, 10)，步长为2，为0,2,4。。。

#导入模块import和使用
import random
for i in range(5):
    print random.randint(1, 10)   #[1, 10]
import sys
sys.exit()   #退出脚本