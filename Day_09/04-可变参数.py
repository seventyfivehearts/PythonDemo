# 可变参数使用 *args 多出来的数据会以元组的形式保存下来
# **kwargs 表示可变的关键字参数

def add(a, b, *args, **kwargs):
    # c = a * kwargs
    # 缺省参数要放在最后面
    # return a + b + args
    print(kwargs)  # 多余的关键字会以字典的形式保存下来


# add(1, 2, 3)
add(1, 2, m=0, n=1)
