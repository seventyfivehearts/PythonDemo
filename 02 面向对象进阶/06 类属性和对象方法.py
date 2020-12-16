# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 22:08
# @Author  : sunzhen
# @File    : 06 类属性和对象方法.py
# @Software: PyCharm

class Person(object):
	# 类对象
	type = '人类'
	
	def __init__(self, name, age):
		self.name = name
		self.age = age


# p1,p2称之为实例对象,在内存中各自分配空间
# Person 自己分配一个内存空间,称之为类对象
# 只要创建了一个实例对象,那么这个示例对象
# 就有自己的属性
#
# name age 是对象属性, 是每一个示例对象都会
# 单独保存一份的属性
# 每个实例对象的之间的属性没有关联,互不影响

p1 = Person('张三', 19)
p2 = Person('李四', 20)

# 类属性可以通过类对象和实例对象获取
print(Person.type)  # 人类

# 也可以通过实例对象获取类属性
print(p1.type, p2.type)  # 人类 人类

p1.type = '你好'
print(p1.type)  # 并不会修改类属性,而是给示例对象添加了一个新的对象属性

# 类属性只能通过类对象来修改,实例对象无法修改类属性

Person.type = 'Python'
print(Person.type)  # Python,修改了类属性
