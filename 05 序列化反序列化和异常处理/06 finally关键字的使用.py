# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 15:02
# @Author  : sunzhen
# @File    : 06 finally关键字的使用.py
# @Software: PyCharm
try:
	file = open('names.txt', 'rb')
	while True:
		content = file.read(1024)
		if not content:
			break
		print(content)
finally:  # 最终都会指定的代码
	print('文件被关闭了')
	file.close()

# 函数中的finally会覆盖之前的返回值，返回finally下的值
