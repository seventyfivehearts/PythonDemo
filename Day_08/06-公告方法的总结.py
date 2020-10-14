# 算数运算符
#  + 用于字符串 元组 列表的拼接 不能用集合和字典
print('hello' + 'world')
print(('good',) + ('happy',))
print([1, 2, 3] + [4, 5, 6])

#  - 用于集合求差集
print({1, 2, 3} - {1})

# 乘法 用字符串元组列表 用于重复多次  不能用于字典和集合
# 字典和集合是无序的
print('hello' * 2)
print([1, 23, 3] * 3)
print((1, 3, 2) * 3)

# in 运算符


# 带下标的遍历 enumerate 列表元组

nums = [1, 2, 4, 5, 6]
print(enumerate(nums))
for i, e in enumerate(nums):
    print(i, e)
