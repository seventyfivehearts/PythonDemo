# 使用bool内置类将其他数据转换为bool类型
print(bool(100))

# 在数字里面，只有0被转换为布尔值为False，其他转换为布尔值是True

# 字符串中只有 “” 或者‘’ 可以转换为False，其他为True
# None 转换为bool 为False
print(bool(None))

print(bool([]))
print(bool(()))
print(bool({}))  # False
if 3:
    print('hello')

    