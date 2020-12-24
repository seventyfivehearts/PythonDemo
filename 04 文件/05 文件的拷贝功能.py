# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:31
# @Author  : sunzhen
# @File    : 05 文件的拷贝功能.py
# @Software: PyCharm
import os

# 如果输入的文件不存在会报错


file_name = input('请输入一个文件路径')
if os.path.isfile(file_name):
	old_file = open(file_name)
	
	new_file = 'sss.txt'
	# 名字的拼接
	# names = new_file.rpartition('.') # ('xxx', '.', 'txt')
	# new_file_name = names[0] + '.bak.' + names[2]
	
	names = os.path.splitext(file_name)  # ('xxx', '.txt')
	new_file_name = names[0] + '.bak' + names[1]
	new_file = open(new_file_name, 'w')
	
	new_file.write(old_file.read())
	
	new_file.close()
	old_file.close()
	
else:
	print('输入的文件不存在')
