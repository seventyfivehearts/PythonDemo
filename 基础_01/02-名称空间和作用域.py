# 示范1
# def fuc():
#     print(x)
#
# x = 111
# fuc()

# 名称空间的关系   以函数定义阶段为准 与函数调用位置无关
# x = 111
# def func():
#     print(x)
#
# def foo():
#     x = 222
#     func()
#
# foo()
# 示例3： 函数嵌套的定义

# 函数调用都要回到函数最开始定义的地方


# 示范4：函数嵌套关系一定要以函数定义阶段为准
# 变量要先定义后使用
# x = 111
# def func():
#     print(x)
#     x = 222
#
#
# func()
# UnboundLocalError: local variable 'x' referenced before assignmentUnboundLocalError: local variable 'x' referenced before assignment


# 二:作用域->作用范围
# 全局作用域： 内置名称空间、全局名称空间
# 1.全局存活
# 2.全局有效:被所有函数共享
def foo():
    x = 111
    print(x)
def func():
    y = 111
    print(y)
# 局部作用域
# 局部名称空间的名字
# 1.临时存活
# 2.局部有效:函数内有效


# LEGB
# builtin(内置)
# global(全局)
def f1():
    # enclosing(局部)
    def f2():
        # local(当前的)
        def f3():
            pass
























































































