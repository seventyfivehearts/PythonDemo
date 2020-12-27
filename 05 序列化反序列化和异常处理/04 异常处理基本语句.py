# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:07
# @Author  : sunzhen
# @File    : 04 异常处理基本语句.py
# @Software: PyCharm

# try:
# except:

def div(a, b):
	return a / b


try:
	x = div(5, 0)
except Exception as e:
	print('程序出错了')
else:
	print(x)
