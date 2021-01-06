# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 15:37
# @Author  : sunzhen
# @File    : mod.py
# @Software: PyCharm
class Teacher(object):
	def __init__(self, name, password):
		import tools
		self.name = name
		self.password = tools.encrypt_password(password)


class Student(object):
	def __init__(self, s_id, name, age, gender, tel):
		self.s_id = s_id
		self.name = name
		self.age = age
		self.gender = gender
		self.tel = tel
	

