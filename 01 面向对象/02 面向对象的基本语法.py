# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 21:40
# @Author  : sunzhen
# @File    : 02 面向对象的基本语法.py
# @Software: PyCharm

# 类和对象

# 小明今年18 岁，身高 1.75，每天早上跑完步，会去 吃 东西
# 小美今年17 岁，身高 1.65，小美不跑步，小美喜欢 吃 东西


# 1.定义类(驼峰命名) 使用class来定义一个类
# class 类名
# 	class<类名>:
# 	class<类名>(object):
class Students:  # 类中要关注这个类有哪些属性和行为
	def __init__(self, name, age, height):
		# __init__方法中以参数的形式定义特征，称之为属性
		self.name = name
		self.age = age
		self.height = height
	
	# 行为定义为函数
	def run(self):
		print('正在跑步')
	
	def eat(self):
		print('正在吃饭')


# Students() -> 自动调用init方法
# 使用Students 类创建两个示例对象 s1, s2(都有属性和方法)
s1 = Students('小明', 18, 1.83)
s2 = Students('小美', 19, 1.63)

s1.run()
s1.eat()

s2.run()





