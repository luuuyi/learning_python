import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print '哈哈哈'

#coding=utf-8
# Python2.7默认情况使用整形计算
print 11 + 5, (5+1)*2/3

#Python中的三种常见数据类型
print -2, -1.25, 'ssdsds'

#字符串连接，接受的操作符为+和*
print 'fdfdsf' + 'dsfsd'
print 'fdsff' + 43   # 错误的
print 'fdsfds' * 5
print 'dsda' * 'dafds' # 错误的

#使用变量保存值
sum = 0
sum_1 = sum + 1
name = 'jack'

#变量名不允许有如下
print 'a-b', 'a b', '4ab', '4', '$'

#几个常用的函数
print len('dsgfdsfds')
print 'saff' + str(244) + 'dfs'
print int(34.5) + float(34)

#判断语法的问题，数值怎么计算都是相等的
print 42 == '42'   #False
print 43 == 43.0   #True