# 元组 用来保存多个数据 使用() 表示
# 不可变数据类型
nums = (1, 3, 5, 9, 0, 0, 0, 0)
# 可以使用下标来获取元素
print(nums[4])
# 不能通过下标来更改数据类型
# nums[2] = 10
# 'tuple' object does not support item assignment
print(nums)

# index() 输出元素的下标
print(nums.index(9))
# count() 输出元素在元组中出现的次数
print(nums.count(0))

# 特殊情况 怎么表示一个元组
a = (18)
print(type(a))  # <class 'int'>
age = (18,)
print(type(age))  # <class 'tuple'>

# tuple内置类  tuple()括号里面需要是 可迭代对象
# print(tuple(18))   #TypeError: 'int' object is not iterable
print(tuple('hello'))  # ('h', 'e', 'l', 'l', 'o')

# 列表转换为元组  元组转换为列表
# 列表转换为元组
# 使用内置类 tuple
a = ['hello', 'hhh', 'happy', 'hey']
print(tuple(a))  # ('hello', 'hhh', 'happy', 'hey')


# 使用 join
height = ('180','200','165')
print('*'.join(height))
print("".join(('h', 'e', 'l', 'l', 'o')))

# 元组也可以遍历

for i in nums:
    print(i)

j = 0
while j < len(nums):
    print(nums[j])
    j += 1
