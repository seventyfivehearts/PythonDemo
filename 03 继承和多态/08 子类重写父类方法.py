# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:42
# @Author  : sunzhen
# @File    : 08 子类重写父类方法.py
# @Software: PyCharm

class Person(object):
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sleep(self):
		print(self.name + '正在睡觉')


class Student(Person):
	
	def __init__(self, name, age, school):
		# self.name = name
		# self.age = age
		# self.school = school
		# 子类在父类的方法上添加新功能
		# 1.父类名.方法名(self,参数列表)
		# Person.__init__(self, name, age)
		# 2.super 调用父类， 推荐使用
		super(Student, self).__init__(name, age)
		self.school = school
	
	def sleep(self):
		print(self.name + '正在课间睡觉')
	
	def study(self):
		print(self.name + '正在学习')


s1 = Student('张三', 20)  # 调用父类的 __init__方法
s1.sleep()  # 调用父类的方法
# __mro__
print(Student.mro())
# 从自己开始找
# [<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]

# 子类重写父类方法的情况
# 1. 子类和父类的方法完全不一样
# 2. 子类的方法在父类的基础上有增加