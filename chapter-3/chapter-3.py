import os

#定义函数使用def
def hello():
    print 'hello'

hello()

def whoami(name):
    print name
    return len(name)

x = whoami('name')

#局部作用域和全局作用域
def name(x):
    x = 'kkk'
    print x

name('s')
print x   # 错误的

#局部作用域的优先级大于全局作用域
def name():
    x = 'kkk'
    print x

x = 'i'
name()  #kkk
print x #i

#Python系统的异常处理，使程序能够自动化部署时应对可能的异常
def divide(num):
    try:
        x = 10 / num
    except ZeroDivisionError:
        print 'num = 0'