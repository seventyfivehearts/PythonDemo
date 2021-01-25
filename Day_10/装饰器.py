# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 21:26
# @Author  : sunzhen
# @File    : 装饰器.py
# @Software: PyCharm

# def foo():
# 	print('foo')
#
#
# foo()  # foo
# print(foo)  # <function foo at 0x0000027802C19EE0>

# def foo():
# 	print('foo')
#
#
# foo()  # foo
# foo = lambda x: x + 1
# # 把匿名函数赋值给foo之后，原本的函数的内存地址改变为新赋值的
# print(foo)  # <function <lambda> at 0x000001C667759A60>


# 开发中要遵循 开放封闭原则
# 封闭 对以开发的功能封闭
# 开放 对扩展的功能开放

# def w1(func):
#     def inner():
#         # 验证1
#         # 验证2
#         # 验证3
#         func()
#     return inner
#
# @w1
# def f1():
#     print('f1')
# @w1
# def f2():
#     print('f2')
# @w1
# def f3():
#     print('f3')
# @w1
# def f4():
#     print('f4')
# def w1(func):
# 	def inner():
# 		# 验证1
# 		# 验证2
# 		# 验证3
# 		func()
#
# 	return inner
#
#
# @w1
# def f1():
# 	print('f1')


# print(f1)  # <function w1.<locals>.inner at 0x0000026A3596E4C0>
# 此地址为添加装饰器之后的地址

# @ w1    执行 w1函数, 将 w1下的函数当作参数传递给 w1()函数中的func
# @ w1  ==> w1(f1)
# 此时的func = f1    func() = f1()

#
# def makeBoid(func):
# 	def wrapper():
# 		return '<b>' + func() + '</b>'
#
# 	return wrapper
#
#
# def makeIctlin(func):
# 	def wrapper():
# 		return '<a>' + func() + '</a>'
#
# 	return wrapper
#
#
# @makeIctlin
# def test1():
# 	return '111111'
#
#
# @makeBoid
# def test2():
# 	return '222222'
#
#
# @makeBoid
# @makeIctlin
# def test3():
# 	return '3333333'
#
#
# print(test1())
# print(test2())
# print(test3())
#
# # <a>111111</a>
# # <b>222222</b>
# # <b><a>3333333</a></b>

# # 无参装饰器
# def check(func):
# 	def wrapper():
# 		return '早点' + func()
#
# 	return wrapper
#
#
# @check
# def go_to_bed():
# 	return '去睡觉'
#
#
# print(go_to_bed())
# # 早点去睡觉

# # 被装饰的函数有参数
# def check(func):
# 	def wrapper(name, action):
# 		return '我说' + func(name, action)
# 	return wrapper
#
#
# @check
# def go_to_bed(name, action):
# 	return name + '去睡觉' + action
#
#
# print(go_to_bed('张三', '在家'))
# # 我说张三去睡觉在家


# 被装饰的函数参数不定长
def check(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	
	return wrapper


@check
def demo(*args):
	sum = 0
	for i in args:
		sum += i
	print(sum)


print(demo(1, 2, 3))
