# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 21:15
# @Author  : sunzhen
# @File    : 05 把对象当作字典使用.py
# @Software: PyCharm

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __setitem__(self, key, value):
		print('setitem被调用了,key={},value={}'.format(key, value))
		# 修改 name的值需要先把p1转为字典,在使用
		# 如果不,直接使用[]会出现递归调用的问题,一直调用setitem
		# 不能使用 self.name 写死,要用上面的方法
		p1.__dict__[key] = value
	
	def __getitem__(self, item):
		return self.__dict__[item]


p1 = Person('张三', 19)

print(p1.__dict__)  # 把对象转换成为字典 {'name': '张三', 'age': 19}

# 但是不能直接把一个对象当作字典使用
p1['name'] = 'jack'  # 会调用setitem方法

print(p1.name)

print(p1['name'])  # 会调用getitem方法
