a = 10
b = 20

# 使用第三方变量实现
# c = b
# b = a
# a = c
print(a)
print(b)

# 使用python特有的
a, b = b, a
