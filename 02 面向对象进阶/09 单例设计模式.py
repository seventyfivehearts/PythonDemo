# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 15:59
# @Author  : sunzhen
# @File    : 09 单例设计模式.py
# @Software: PyCharm

class Singleton(object):
	__instance = None
	__is_first = True
	
	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			# cls的作用 申请内存，创建一个对象，并把对象的类型设置为cls
			__instance = object.__new__(cls)
		return cls.__instance
	
	def __init__(self, name, age):
		if self.__is_first:
			
			self.name = name
			self.age = age
			self.__is_first = False


# 调用 __new__方法申请内存
# 如果不重写 __new__方法,会调用object的 __new__方法
# object的__new__方法会申请内存
# 如果重写了 __new__ 方法，需要自己手动申请内存
s1 = Singleton('张三', 19)
s2 = Singleton('李四', 19)

print(type(s1))  # <class '__main__.Singleton'>

# 使其返回 true
print(s1, s2)  # None None

print(s1 is s2)
