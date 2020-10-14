# 使用递归求n!
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


print(fac(6))


# 使用递归求斐波那契数列的第n个数字
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n - 1) + f(n - 2)


print(f(8))
