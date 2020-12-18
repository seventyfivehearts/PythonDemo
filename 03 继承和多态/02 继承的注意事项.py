# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:39
# @Author  : sunzhen
# @File    : 02 继承的注意事项.py
# @Software: PyCharm
class A(object):
	def demo_a(self):
		print('我是demo_a')


# 如果不写继承自谁，在Python3中默认的是object
class B(object):
	def demo_b(self):
		print('我是demo_b')


# Python中支持多继承,继承自谁就可以了
# 如果不同类中有相同的方法，可以使用类属性来查看相关的顺序，按照得到顺序在那个类找到相关方法就使用那个
# 如果没有就报错
class C(A, B):
	pass


# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__)

c1 = C()

c1.demo_a()
c1.demo_b()
