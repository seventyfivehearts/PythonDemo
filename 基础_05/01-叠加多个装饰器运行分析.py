# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 14:06
# @Author  : sunzhen
# @File    : 笔记-叠加多个装饰器运行分析.py
# @Software: PyCharm


# 1.叠加多个装饰器的加载，运行分析(了解)(***)

def deco1(func1):   # func1=wrapper2函数的内存地址
    def wrapper1(*args, **kwargs):
        print('正在运行===>deco1.wrapper1')
        res1 = func1(*args, **kwargs)
        return res1

    return wrapper1


def deco2(func2):   # func2=wrapper3函数的内存地址
    def wrapper2(*args, **kwargs):
        print('正在运行===>deco2.wrapper2')
        res2 = func2(*args, **kwargs)
        return res2

    return wrapper2


def deco3(x):
    def outer3(func3):  # func3=被装饰对象index函数的内存地址
        def wrapper3(*args, **kwargs):
            print('正在运行===>deco3.wrapper3')
            res3 = func3(*args, **kwargs)
            return res3

        return wrapper3

    return outer3


@deco1  # index=deco2(wrapper2的内存地址)==>wrapper1的内存地址
@deco2  # 得到下面函数的内存地址  index=deco3(wrapper3的内存地址)==>index=wrapper2的内存地址
@deco3(111)  # @outer3==>index=outer3(index) ==>index=wrapper3的内存地址
def index(x, y):
    print(x, y)


# 验证内存地址
print(index)  # <function deco1.<locals>.wrapper1 at 0x00000268CD0A71F0>

index(1, 2)

# 加载顺序是自下而上的

# 执行顺序 自上而下
#       :调用index是 wrapper1(1,2)
#       1.wrapper1调用到函数func1的时候是wrapper2的内存地址,调用wrapper2
#       紧接着调用wrapper3的函数的内存地址
#       最后调用index,然后index结束,wrapper3结束,wrapper2结束,wrapper1结束

