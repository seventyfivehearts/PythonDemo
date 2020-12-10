# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 17:12
# @Author  : sunzhen
# @File    : 练习.py
# @Software: PyCharm


class School:
	school_name = '北华大学'
	
	def __init__(self, nickname, addr):
		self.nickname = nickname
		self.addr = addr
		self.classes = []
	
	# class_obj，包含name course
	def related_class(self, class_obj):
		# self.classes.append(class_name)
		self.classes.append(class_obj)
	
	def info_class(self):
		print(self.nickname)
		for class_obj in self.classes:
			class_obj.info_course()


# 一、学校
# 1.创建学校
school_obj1 = School('南校区', '江南')
school_obj2 = School('北校区', '江北')

# 班级
# 2.创建班级
# 江南 南校区
school_obj1.related_class('一班')
school_obj2.related_class('二班')

# 江南 东校区
school_obj2.related_class('一班')

# 3.查看每个校区开设的班级
school_obj2.info_class()


# 关联课程
class Class:
	def __init__(self, name):
		self.name = name
		self.course = None
	
	def related_course(self, class_obj):
		# self.course = course_name
		self.course = class_obj
	
	def info_course(self):
		print('%s%s' % (self.name, self.course))


# 班级操作
class_obj1 = Class('一班')
class_obj2 = Class('二班')
class_obj3 = Class('一班')

# 2.为班级关联一个课程
class_obj1.related_course('Python开发')
class_obj2.related_course('Linux开发')
class_obj3.related_course('Python开发')

# 3.查询班级开设的课程
# class_obj1.info_course()
# class_obj2.info_course()
# class_obj3.info_course()


# 2.为学校开设班级
# 江南 南校区
school_obj1.related_class(class_obj1)
school_obj2.related_class(class_obj1)

# 江南 东校区
school_obj2.related_class(class_obj2)


# print(school_obj1.classes)

class Course:
	pass


class Students:
	pass
