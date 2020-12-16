# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 20:59
# @Author  : sunzhen
# @File    : 04 内置属性.py
# @Software: PyCharm

class Person(object):
	# 规定一定要出现的属性
	__slots__ = ('name', 'age')
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def eat(self):
		print(self.name + '正在吃东西')


p1 = Person('张三', 19)

# 把所有的属性显示出来
print(dir(p1))
'''
['__class__', '__delattr__', '__dict__'
 '__dir__', '__doc__', '__eq__'
 '__format__', '__ge__'
 '__getattribute__', '__gt__'
 '__hash__', '__init__', '__init_subclass__'
'__le__', '__lt__', '__module__', '__ne__'
 '__new__', '__reduce__', '__reduce_ex__'
 '__repr__', '__setattr__', '__sizeof__'
 '__str__', '__subclasshook__'
 '__weakref__', 'age', 'eat', 'name']
'''

print(p1.__doc__)  # 输出类说明的文档
print(Person.__doc__)

# 模块
print(p1.__module__)  # __main__



