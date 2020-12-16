# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 23:19
# @Author  : sunzhen
# @File    : test.py
# @Software: PyCharm


# 编写一个函数,求多个数中的最大值
def get_max(*args):
	x = args[0]
	for arg in args:
		if arg > x:
			x = arg
	return x


print(get_max(2, 6, 4, 3))
