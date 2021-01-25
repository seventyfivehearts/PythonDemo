def add(a, b):
	return a + b
#
#
# x = add(2, 5)
#
# fn = add  # 相当于给函数fn 起一个别名
# print(fn(2, 3))
#
# # lambda  定义一个函数
# # 匿名函数  用来表示简单的函数,调用次数很少基本上只用一次
#
# # 调用匿名函数的方式
# # 1.给他定义一个名字(很少使用)
# mul = lambda a, b: a + b
# print(mul(2, 3))
#
#
# 2.把匿名函数当作一个参数传递给另一个函数使用(使用场景比较多)
def clc(a, b, obj):
	print(a, b, obj)


obj = lambda a, b: add(a, b)
clc(1, 2, (3, 4))
