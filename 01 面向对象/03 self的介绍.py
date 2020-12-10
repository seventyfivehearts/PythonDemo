# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 22:23
# @Author  : sunzhen
# @File    : 03 self的介绍.py
# @Software: PyCharm

class Student(object):
	
	# 这个属性直接定义再类里面，是一个元组，用来规定对象可以存在的属性
	# 如果不添加会报错
	__slots__ = ('name', 'age', 'city')
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def say_hello(self):
		print('hello', self.name)


# Student('张三', 18) 具体做了什么？
# 1.调用 __init__ 方法用来申请内存空间
# 2.自动调用__init__方法传入参数，将self指向创建好的内存空间，填充数据
#  谁调用 self 谁就是 self
s1 = Student('张三', 18)
print(s1.name)

s1.say_hello()

print(s1.name)

# print(s1.heigiht)  # AttributeError: 'Student' object has no attribute 'heigiht'
# 没有这个属性

# 动态属性
# 直接用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 如果存在，会修改这这个属性的值

s1.city = '上海'  # 给对象添加这个属性对应的值
print(s1.city)

