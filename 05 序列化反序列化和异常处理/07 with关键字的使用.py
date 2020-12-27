# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 15:03
# @Author  : sunzhen
# @File    : 07 with关键字的使用.py
# @Software: PyCharm
# try:
#
# 	file = open('names.txt', 'r')
# except FileNotFoundError:
# 	print('文件不存在')
# 	try:
# 		file.read()
# 	finally:
# 		file.close()

# 更简便的方法使用with
# with关键字可以帮助我们把文件关闭，但是如果不能判断文件存不存在
try:
	with open('names.txt', 'r') as file:
		file.read()
except FileNotFoundError:
	print('文件不存在')
