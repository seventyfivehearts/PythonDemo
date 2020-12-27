# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 14:38
# @Author  : sunzhen
# @File    : 练习1.py
# @Software: PyCharm
import math

class Pointer(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Circle(object):
	def __init__(self, cp, radius ):
		self.radius = radius
		self.cp = cp
		
	def area(self):
		return self.radius ** 2 * math.pi
	
	def length(self):
		return self.radius * 2 * math.pi


p = Pointer(0, 0)  # 创建一个Point对象
c = Circle(p, 4)  # 创建一个CirCle对象,并把P传进去

print(c.area())
print(c.length())
