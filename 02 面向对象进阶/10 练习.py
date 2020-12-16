# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 17:32
# @Author  : sunzhen
# @File    : 10 练习.py
# @Software: PyCharm

# 定义一个类属性,记录创建了多少个类对象
class Person(object):
	count = 0
	
	def __init__(self, name, age):
		Person.count += 1
		self.name = name
		self.age = age

# 每次创建对象，都会调用__new__ 方法和 __init方法
# 调用 __new__方法，用来申请内存空间
# 如果不重写 __new__方法，会自动找object的new方法
# object的new方法,默认实现是申请一段内存,创建一个对象


p1 = Person('张三', 18)
p2 = Person('李四', 20)
p3 = Person('周五', 21)
print(Person.count)
