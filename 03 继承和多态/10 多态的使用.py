# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:42
# @Author  : sunzhen
# @File    : 10 多态的使用.py
# @Software: PyCharm

class Dog(object):
	def work(self):
		print('狗正在工作')

class Dog1(Dog):
	pass


class Dog2(Dog):
	pass


class Dog3(Dog):
	pass


class Person(object):
	def __init__(self, name):
		self.name = name
		self.dog = None
	
	def work_with_dog(self):
		if self.dog is not None and isinstance(self.dog,Dog):
			self.dog.work()


p = Person('张三')

d1 = Dog1()
p.dog = d1
p.work_with_dog()

d2 = Dog2()
p.dog = d2
p.work_with_dog()

d3 = Dog3()
p.dog = d3
p.work_with_dog()
