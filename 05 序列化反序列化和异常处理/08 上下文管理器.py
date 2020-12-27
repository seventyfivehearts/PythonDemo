# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 20:25
# @Author  : sunzhen
# @File    : 08 上下文管理器.py
# @Software: PyCharm

# with关键字的语句需要重写 __enter__ 和 __exit__方法
# 进入到with 代码块时候会调用 __enter__ 方法
# 结束的时候会调用__exit__方法

class Hello(object):
	def __enter__(self):
		# <__main__.Hello object at 0x000001CD58678640>
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass


def func():
	a = Hello()
	return a


# h = Hello.__enter__()
#
with func() as h:
	# h 是 创建对象调用 __enter__方法之后的返回结果
	print(h)
