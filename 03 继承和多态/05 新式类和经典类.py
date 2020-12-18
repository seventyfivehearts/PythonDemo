# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 15:40
# @Author  : sunzhen
# @File    : 05 新式类和经典类.py
# @Software: PyCharm

# 括号里加object 表示子类的父类是 Object
class Person(object):
	pass


# 没有指定父类，在Python3中默认是 object
class Student:
	pass

# 新式类和经典类
# 新式类: 继承自object
# 经典类: 不继承自object

# Python2中如果不指定继承 object则为经典类
# Python3中不存在经典类，只有新式类
