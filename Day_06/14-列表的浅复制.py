import copy

x = [100, 200, 300]
y = x  # x赋值给y,这个时候x,y指向同一个内存地址

# 使用内存空间不一样的  使用 copy 内容一样，指向的空间不一样
z = x.copy()
print(z)
print(id(x))
'''
[100, 200, 300]
2516632011136
2516630953344
'''
print(id(z))

# 使用Python的方法
a = copy.copy(x)  # 相当于浅拷贝
b = x.copy()
print(a)
print(b)
