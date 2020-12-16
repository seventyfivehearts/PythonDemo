# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 22:53
# @Author  : sunzhen
# @File    : 07 私有属性和方法的使用.py
# @Software: PyCharm
import datetime


class Person(object):
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		# 以两个下划线开始的是私有变量
		self.__money = 100
	
	def get_money(self):
		print('{}查询了余额'.format(datetime.datetime.now()))
		return self.__money
	
	def set_money(self, qian):
		print('修改余额')
		self.__money = qian
	
	def __test(self):
		# 		以两个下划线开始的函数,是私有函数,在外部无法调用
		pass


p = Person('张三', 19)

# 其中的name, age在类的外面拿到 p
print(p.name)
print(p.age)
# 私有属性
# 以两个下划线开始的是私有变量 不能直接获取到

# 获取私有属性的方式
# 目的是 '记录'
# 1. 使用对象._类名__私有变量获取
print(p._Person__money)

# 2.通过get set 方法获取
# 	def get_money(self):
# 		return self.__money
print(p.get_money())

p.set_money(100)
