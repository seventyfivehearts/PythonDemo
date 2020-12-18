# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:40
# @Author  : sunzhen
# @File    : 04 私有属性的继承特点.py
# @Software: PyCharm

class Animal(object):
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def eat(self):
		print(self.name + '正在吃好吃的')
	
	def __test(self):
		print('Animal中的私有方法')


class Person(Animal):
	def __demo(self):
		print('Person中的私有方法')

# 私有方法 子类不会继承
p1 = Person('张三', 19)
print(p1.name)
p1._Person__demo()  # 类里面私有方法调用 对象名_类名__私有方法名
p1._Animal__test()
# p1.__test()  # 'Person' object has no attribute '__test'
