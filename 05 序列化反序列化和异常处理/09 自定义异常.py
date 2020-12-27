# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 20:38
# @Author  : sunzhen
# @File    : 09 自定义异常.py
# @Software: PyCharm

# 获取输入的密码 要求 大于6位小于12位

# class ValueError(Exception):
#     """ Inappropriate argument value (of correct type). """
#     def __init__(self, *args, **kwargs): # real signature unknown
#         pass

class Error(Exception):
	pass


password = input('输入密码：')
if 6 < len(password) < 12:
	print('密码正确')
else:
	raise Error('密码错误')

# __main__.Error: 密码错误
