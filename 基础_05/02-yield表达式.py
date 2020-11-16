# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 15:42
# @Author  : sunzhen
# @File    : 02-yield表达式.py
# @Software: PyCharm

# x=yield 返回值 (只能在函数内使用)
# 不写返回值默认是None
# 一.
# def dog(name):
#     print('dog%s准备吃东西了' % name)
#     while True:
#         # x拿到的是yield拿到的返回值
#         x = yield
#         print('dog %s 吃了 %s' % (name, x))
#
#
# #     只要调用yield,就跟函数内没关系了
# a = dog('aaa')
#
# print(a)  # 最后会得到一个生成器
#
# # res = next(a)
# # print(res)
# # next(a)
#
#
# #   TypeError: can't send non-None value to a just-started generator
# a.send(None)  # 相当于next(a)  初始必须要有
#
# a.send('哈哈哈哈哈')
# a.send('包子')
# # 关闭之后无法传值
# a.close()
# a.send('11')  # Traceback (most recent call last):
# # File "D:/PycharmDemo/Demo/基础_05/02-yield表达式.py", line 34, in <module>
# #   a.send('11')
# # StopIteration

# 二.
# def dog(name):
#     print('dog%s准备吃东西了' % name)
#     while True:
#         # x拿到的是yield拿到的返回值
#         x = yield 1111
#         print('dog %s 吃了 %s' % (name, x))
#
#
# a = dog('name')
# res = a.send(None)
# print(res)
#
# a.send('你好')

# 先从当前位置收到一个值赋值给x,如a.send(None) next(a),本次yield碰到新的运行值再把值返回给x

# def func():
#     print('start')
#     x = yield 1111  # xxxxx
#     print('end')
#     yield 2
#
# g = func()
# next(g)
# res = next(g)
# print(res)
#
# res = g.send('xxxxx')
# print(res)