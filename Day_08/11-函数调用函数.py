# 定义一个函数,求[n,m)之间的和
def add(n, m):
    x = 0
    for i in range(n, m):
        x += i
        return x


print(add(1, 3))
