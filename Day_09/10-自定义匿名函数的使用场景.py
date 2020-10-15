def calc(a, b, fn):
    c = fn(a, b)
    return c


# 添加的参数是函数类型的参数(fn)
# 回调函数


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


x1 = calc(1, 3, add)
print(x1)
x2 = calc(2, 3, minus)
# 在函数调用的方法比较简单,只使用几次 可以使用 lambda函数来写
x3 = calc(1, 2, lambda x, y: x + y)
x4 = calc(2, 3, lambda x, y: x * y)
print(x4)