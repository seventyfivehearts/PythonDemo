# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:42
# @Author  : sunzhen
# @File    : 09 不使用多态的问题.py
# @Software: PyCharm

# 多态基于继承中子类重写父类的方法，实现 子类调用父类的方法得到不同的结果 提高代码的灵活性

class Police_dog(object):
	def attack_enemy(self):
		print('警犬正在工作')


class Person(object):
	def __init__(self, name, dog):
		self.name = name
		self.dog = dog
		
	def person_and_dog(self):
		self.dog.attack_enemy()
		

pd = Police_dog()
p1 = Person('张三', pd)
p1.person_and_dog()
print(hex(id(pd)),hex(id(p1)))