# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 16:33
# @Author  : sunzhen
# @File    : 01-无参装饰器.py
# @Software: PyCharm

# 储备知识
# *args **kwargs
# def index(x, y):
#     print(x, y)


# def wrapper(*args, **kwargs):
#     index(*args, **kwargs)


# wrapper(x=11, y=22)


# 2.名称空间与作用域
# 名称空间的’嵌套‘关系是确定在函数定义阶段，即检测语法阶段

# 3.函数对象:可以把函数当做参数传入,把函数当成返回值返回(函数的内存地址)
# def index():
#     return 123
#
#
# def foo(func):
#     print(func)
#
#
# foo(index)
# 函数的嵌套定义
#     在一个函数内可以定义另一个函数
# def outer():
#     def wrapper():
#         pass
#     return wrapper
# 闭包函数

# 把一个函数封闭在函数中
# def outer():
#     x = 111
#
#     def wrapper():
#         x
#
#     return wrapper
#
#
# f = outer()

# 传参的方式一：通过参数的形式为函数传值
# def wrapper(x):
#     print(1)
#     print(2)
#     print(3)
#     x
#
# # 通过定义参数的方式传参
# wrapper(1)
# 传参的方式二：通过闭包的方式为函数体传参
# def outter(x):
#     def wrapper():
#         print(1)
#         print(2)
#         print(3)
#         x
#
#
#     return wrapper
#
#
# f = outter(1)


# 二 装饰器
"""
1.什么是装饰器
    器 指的是工具，比如函数，类
    装饰指的是为其他事物添加额外的东西点缀

    合在一起
        装饰器指的是定义的一个函数
        该函数时用来装饰其他函数的
        为其他函数增加功能的
2.为何要用装饰器(在不修改源代码的情况下添加新功能)
    开放封闭原则
       开发：对拓展功能是开放的
       封闭：对修改源代码是封闭的

       在开发过程中，如果功能不需要修改，则不要修改源代码
       装饰器就是在不修改被装饰对象源代码
       以及调用方式的情况下为被装饰对象添加新功能

3.如何使用装饰器
"""


# 需求 在不修改源代码的前提下为其添加统计
#   运行时间的功能

# def index(x, y):
#     print('index %s %s' % (x, y))
#
#
# index(111, 222)
# 统计函数的运行时间

# 解决方案一：失败
# 问题 修改了源代码
# import time
#
#
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     stop = time.time()
#     print(stop - start)
#
#
# index(11, 22)

# 解决方案二：
# 问题:没有修改被装饰对象的调用方式
#       也没有修改源代码，并且加上了新功能
#       但是代码冗余


# import time
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop - start)

# 解决方案三
# 问题:解决了冗余的问题，但出现新的问题
#       函数调用方式改变

# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#
# def wrapper():
#     start = time.time()
#     index(111, 222)
#     stop = time.time()
#     print(stop - start)
#
# wrapper()


# 解决方案三优化：如何在方案三的基础上不改变函数调用方式
# import time
#
#
# def index(x, y, z):
#     time.sleep(3)
#     print('index %s %s %s' % (x, y, z))
#
#
# def wrapper(*args, **kwargs):
#     # 通过此方式为index传参
#     start = time.time()
#     index(*args, **kwargs)
#     stop = time.time()
#     print(stop - start)
#
#
# wrapper()

# 方案三的优化二，在优化一的基础上
#     把装饰对象写活了，原来只能装饰index
# import time
#
#
# def index(x, y, z):
#     time.sleep(3)
#     print('index %s %s %s' % (x, y, z))
#
#
# def home(name):
#     time.sleep(2)
#     print('%s' % name)
#
#
# def outer(func):
#     # func = index
#     def wrapper(*args, **kwargs):
#         # 通过此方式为index传参
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#
#     return wrapper
#
#
# index = outer(index)  # index->wrapper的内存地址
#
# index(1, 2, 3)
#
# home = outer(home)  # 此时home指向wrapper的内存地址
#
# home('name')

# 方案的优化三 将wrapper做的跟被装饰对象一摸一样，以假乱真
#
# import time
#
#
# def index(x, y, z):
#     time.sleep(3)
#     print('index %s %s %s' % (x, y, z))
#
#
# def home(name):
#     time.sleep(2)
#     print('%s' % name)
#
#     return 123
#
#
# def outer(func):
#     # func = index
#     def wrapper(*args, **kwargs):
#         # 通过此方式为index传参
#         start = time.time()
#         # 设置变量给函数返回值
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#
#     return wrapper
#
#
# home = outer(home)  # 此时home指向wrapper的内存地址
#
# res = home('name')  # res = wrapper('name')
# print('返回值', res)


# 语法糖 让你开心的语法
# import time
#
#
# # 装饰器
# def outer(func):
#     # func = index
#     def wrapper(*args, **kwargs):
#         # 通过此方式为index传参
#         start = time.time()
#         # 设置变量给函数返回值
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#
#     return wrapper


# 在被装饰对象正上方单独一行写上@装饰器名字
# @outer
# def index(x, y, z):
#     time.sleep(3)
#     print('%s%s%s' % (x, y, z))
#
#
# @outer
# def home(name):
#     time.sleep(2)
#     print('%s' % name)
#     return 1234
#
#
# index(1, 2, 3)
# home('name')

# 装饰器总结:模板
# def outer(func):
#     def wrapper(*args,**kwargs):
#         # 1.调用原函数
#         # 2.为其增加新功能
#         res = func(*args,**kwargs)
#         return res
#     return wrapper

# import time
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         # 1.调用原函数
#         # 2.为其增加新功能
#         start = time.time()
#         stop = time.time()
#         print(stop - start)
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper


# 认证功能的装饰器
def auth(func):
    def wrapper(*args,**kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        name = input('your name>>:').strip()
        pwd = input('your password>>:').strip()
        if name == 'name' and pwd == '123':
            res = func(*args,**kwargs)
            return res
        else:
            print('账号密码错误')
    return wrapper

@auth
def index():
    print('from index')


index()
