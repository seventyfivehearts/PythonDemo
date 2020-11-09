# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 14:56
# @Author  : sunzhen
# @File    : 02-迭代器.py
# @Software: PyCharm

# 1.迭代器
#     迭代器指的是迭代取值的工具,迭代是一个重复的过程
#     每次重复都是基于上一次的结果继续的,单纯的重复并不是迭代

# 2.为何要有迭代器
# l = ['name', 'hello', 'world']
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

"""
    迭代器是用来迭代取值的工具,而涉及到把多个值循环
    取出来的类型有:
        列表,字符串,元组,字典,集合,打开的文件
        
        
    但是上诉迭代取值的方式只适用于有索引的数据类型
        :列表,字符串,元组
        
    不依赖索引的取值方式
        迭代器    
    
"""

# 3.如何用迭代器
"""
    可迭代对象
        只要内置有__iter__方法的称之为可迭代对象
        (可以转换成迭代器的对象)
"""
# count = 0
# while True:
#     name = input('>>:')
#     print(count)
#     count += 1

# l = ['name', 'hello', 'world']
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1
# 调用可迭代对象下的__iter__方法会将其转换为迭代器对象
# a = {'a': 1, 'b': 2, 'c': 2}
# d_iter = a.__iter__()  # <dict_keyiterator object at 0x0000021D0869DC70>
# print(d_iter)
# d_iter.__next__()
#
# print(d_iter.__next__())
# # print(d_iter.__next__())
# # print(d_iter.__next__())  # 抛出一场StopIteration
#
# while True:
#     try:
#         print(d_iter.__next__())
#     except StopIteration:
#         break
# print('>>>>>>>')  # 在一个迭代器取值取干净的情况下,再对其取值取不到
# # 只能通过再新来一个
# print(d_iter.__next__())
# while True:
#     try:
#         print(d_iter.__next__())
#     except StopIteration:
#         break
# # 字符串,元组,字典,

# 可迭代对象与迭代对象详解
# 可迭代对象(可以转换成迭代器的对象):内置有__iter__对象
#       可迭代对象.__iter__(): 得到迭代器对象

# 迭代器对象:内置有__next__()方法并且内置有__iter__方法的对象
#       迭代器对象.__next__():得到迭代器的下一个值
#       迭代器对象.__iter__():得到迭代器的本身(跟没调用一样)
# dic = {'q':1,'w':2}
# dic_iterator = dic.__iter__()
# print(dic_iterator is dic_iterator.__iter__())  # True


# for循环的工作原理(迭代器循环)
# a = {'a': 1, 'b': 2, 'c': 2}
# d_iter = a.__iter__()
# print(d_iter.__next__())
# while True:
#     try:
#         print(d_iter.__next__())
#     except StopIteration:
#         break
# 1.d_iter.__iter()__得到一个迭代器对象
# 2.迭代器对象.__next__()拿到一个返回值,然后将返回值赋值给k
# 3.重复步骤2,知道抛出StopIteration异常 for循环会捕捉异常然后结束循环
# for k in d_iter:
#     print(k)

# 可迭代对象: 字符串,列表,元组,字典,集合,文件对象
# 迭代器对象: 文件对象

# with open('a.txt',mode='rt',encoding='utf-8')as f:
#     for line in f:
#         print(line)


# list('hello') # 原理同for循环

# 4.迭代器的优缺点
"""
优点
    1.为序列和非序列类型提供了一种统一的迭代取值方式
    2.惰性计算: 迭代器对象表示的是一个数据流,可以只在需要时才去调用next
    算出一个值,就迭代器本身来说,同一时刻内存只有一个值,因而可以存放无线
    大的数据流,而对于其他容器类型,如列表,需要把所有元素都存放于内存中,受内存
    大小的限制,可以存放的值的个数是有限的

缺点:
    1.除非取尽,否则无法获取迭代器的长度
    2.只能取下一个值,不能回到开始,更像是一次性的,迭代器产生后的唯一目标
    就是重复执行next方法,否则就会停留在某个位置,等待下一次调用next,若是要再次迭代
    同一对象,你只能重新调用iter方法去创建一个新的迭代器对象,如果有两个或者
    多个循环使用同一个迭代器,必然只会有一个循环取到值
    
"""

















