# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 14:40
# @Author  : sunzhen
# @File    : 08 类方法和静态方法.py
# @Software: PyCharm

class Person(object):
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def eat(self, food):  # 对象方法有一个参数self,指的是实例对象
		print(self.name + '在吃' + food)
	
	# 如果一个方法里没有用到实例对象的任何属性
	# 可以将这个方法设置成static
	@staticmethod
	def demo():
		print('hello')


p = Person('张三', 19)
# 实例对象在调用方法的时候,不需要给形参self传参
# 会自动把示例对象传递给self

# 1.eat 对象方法,直接使用实例对象.方法名调用
# 使用对象名.方法名(参数) 来进行调用,不需要传self
# 会自动将对象名传递给self
p.eat('好吃的')  # 直接使用实例对象调用方法

# 2.对象方法使用 类对象来调用类名.方法名()
# 但是这种方式不会自动传入参数,需要手动的指定self
Person.eat(p, '饭')

# 静态方法调用方式
Person.demo()
p.demo()

class Cal(object):
	@staticmethod
	def add(a, b):
		return a + b


# 静态方法可以像函数一样调用,通过类名来调用,依附于类来使用的

Cal.add(1, 2)
