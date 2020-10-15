# filter 对可迭代对象进行过滤,得到的是filter对象
# Python2的时候是内置函数,Python3修改成了一个内置类
ages = [12, 3, 4, 22, 34, 53, 18]
# filter 可以给定两个参数,第一个参数是函数,第二个参数是可迭代对象

# <filter object at 0x000002967A1C8910>
# x 是一个filter类型的对象
x = filter(lambda ele: ele > 18, ages)
print(x)

# for i in x:
#     print(i)
# 可迭代对象转换成为列表
adult = list(x)
print(adult)


