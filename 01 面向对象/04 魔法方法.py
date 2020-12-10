# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 16:09
# @Author  : sunzhen
# @File    : 04 魔法方法.py
# @Software: PyCharm

# 魔法方法也称之为魔术方法
# 在类里面的一些特殊方法
# 特点如下
# 1.不需要手动调用，会在何时的时机自动调用
# 2.都是以__开头，__结尾的方法
# 3.方法名字都是系统规定好的，在合适的时机自己调用

class Person(object):
	def __init__(self, name, age):
		# 在创建对象时候，会自动调用这个方法
		print('__init__方法被调用了')
		self.name = name
		self.age = age
	
	def __del__(self):
		# 在对象被销毁的时候会自动调用这个方法
		print('__del__方法被调用了')
	
	def __repr__(self):
		# 自动调用 并返回 hello
		return 'hello'
	
	# 可读性比较好
	def __str__(self):
		return '姓名{},年龄{}'.format(self.name, self.age)
	
	def __call__(self, *args, **kwargs):
		print('call方法被调用了')


p = Person('carter', 19)
# del p 手动删除
print(p)
# 如果不做任何修改，直接打印一个模块名.类型，内存地址
# <__main__.Person object at 0x000002A74CBA8640>

# 当打印一个对象的时候，会调用对象的 __str__ 或者 __repr__方法
# 如果两个方法都写了， 调用 __str__
# __repr__一般不被调用

# 对象名() 调用__call__方法
p()  # 'Person' object is not callable


