nums = [6, 5, 8, 7, 3, 1, 2, 4]

# 排序和反转
# 调用列表的sort方法直接进行排序
# 直接对列表进行排序
# nums.sort()
nums.sort(reverse=True)  # 反转
print(nums)

# sorted 不对原有列表进行改变,生成一个新的原有数据
a = sorted(nums)
print(a)

# 使用内置函数 reverse
name = ['李四', '王五', '张三']
name.reverse()
print(name)
# 使用切片[::-1]
c = name[::-1]
print(c)
