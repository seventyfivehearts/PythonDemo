# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:07
# @Author  : sunzhen
# @File    : 05 异常处理的使用场景.py
# @Software: PyCharm

# 在异常出终止避免出现更多的问题
try:
	file = open('xxx.txt')
	print(file.read())
	file.close()
except Exception as e:  # [Errno 2] No such file or directory: 'xxx.txt'
	print(e)
