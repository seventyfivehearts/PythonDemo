# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:39
# @Author  : sunzhen
# @File    : 01 继承的基本使用.py
# @Software: PyCharm

# 面向对象编程的三大特性: 封装, 继承, 多态
# 封装: 函数是对语句的封装,类是对函数和变量的封装

# 继承: 类和类之间可以认为手动的建立父子关系
# 		父类的属性和方法,子类可以使用

# 多态: 一种技巧,提高代码效率

# class Person(object):
#
# 	def __init__(self):
# 		pass
#
# 	def eat(self):
# 		pass


class Animal(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sleep(self):
		print(self.name + '正在睡觉')


# class Dog(object):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def sleep(self):
# 		print(self.name + '正在睡觉')
#
# 	def dark(self):
# 		print(self.name + '正在叫')
#
#
# class Student(object):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def sleep(self):
# 		print(self.name + '正在睡觉')
#
# 	def study(self):
# 		print(self.name + '在学习')


# 1.调用 __new__ 方法，再调用__init__方法
# 2.子类中没有 __new__方法的时候会查看父类中是否有
class Dog(Animal):
	def dark(self):
		print(self.name + '在叫')


class Student(Animal):
	
	def study(self):
		print(self.name + '正在学习')


d1 = Dog('黑豆', 3)
print(d1.name)
# 父类定义的属性和方法，子类可以直接使用
d1.sleep()  # 黑豆正在睡觉
d1.dark()
