# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 17:06
# @Author  : sunzhen
# @File    : 03 运算符相关的魔法方法.py
# @Software: PyCharm

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __eq__(self, other):
		return self.name == other.name and self.age == other.age
	
	# def __ne__(self, other):  使用!= 符号会自动调用这个符号
	def __gt__(self, other):  # 使用 > 会自动调用这个方法
		return self.age > other.age


p1 = Person('张三', 19)
p2 = Person('张三', 19)

print(p1 == p2)
