# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 17:11
# @Author  : sunzhen
# @File    : 05 运算符相关的魔法方法.py
# @Software: PyCharm


class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = Person('张三', 19)
p2 = Person('张三', 19)

# p1 p2 不是同一个对象
# 比较两个对象是否是同一个对象 比较内存地址是否相同

# 身份运算符 is 比较两个对象是否是同一个对象
# == 会调用对象的__eq__方法,获取这个方法的比较结果

print(p1 is p2)  # False

num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 is num2)  # False
