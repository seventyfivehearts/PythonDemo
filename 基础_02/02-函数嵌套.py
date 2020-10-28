# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 16:56
# @Author  : sunzhen
# @File    : 02-函数嵌套.py
# @Software: PyCharm


# 函数嵌套
# 1.函数的嵌套：在调用函数的过程中又调用其他函数


# 2.函数的嵌套定义：在函数内定义其他函数
# 使函数f2在f1的基础上使用
# def f1():
#     def f2():
#         pass
#


# 示例 圆形
def circle(radius, action=0):
    from math import pi
    # 求周长2*pi*radius
    def permiter(radius):
        return 2 * pi * radius

    # 求面积 pi*(radius**2)
    def area(radius):
        return pi * (radius ** 2)

    if action == 0:
        print('1')
        return permiter(radius)
    elif action == 1:
        return area(radius)



circle(5, action=0)
