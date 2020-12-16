# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 16:53
# @Author  : sunzhen
# @File    : 02 魔法方法的介绍.py
# @Software: PyCharm

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def eat(self):
		print(self.name + '正在吃东西')
