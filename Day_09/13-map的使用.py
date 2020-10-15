ages = [12, 3, 4, 22, 34, 53, 18]
# <map object at 0x000002C01D3B8910>
# map和filter一样是函数,可迭代对象
a = map(lambda ele: ele + 2, ages)
print(a)
x = list(a)
print(x)
