# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:41
# @Author  : sunzhen
# @File    : 07 is & isinstance的使用.py
# @Software: PyCharm

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Student(Person):
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = Person('张三', 19)
p2 = Person('张三', 19)

# 身份运算符 is 本质是比较id(p1) == id(p2) 的内存地址
print(p1 is p2)  # 比较两个对象是否是同一对象

s1 = Student('李四', 20)

# isinstance 可以用来判断一个对象是否由指定的类(父类) 实例化出来的
print(isinstance(s1, Person))  # True
print(isinstance(s1, Student))  # True
