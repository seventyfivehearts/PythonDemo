masters = ['王昭君', '妲己', '小乔', '貂蝉', '西施']

# 删除 修改 查询


# 删除数据的方法 pop remove clear

# pop 默认会删除列表的最后一个数据,并且返回数据
# pop(index) 传入索引 index 用来删除指定位置上的数据
# x = masters.pop(2)
# print(x)
# print(masters)

# remove  如果数据在列表中不存在 会报错
masters.remove('王昭君')
print(masters)

# clear 用来情况一个列表
masters.clear()
print(masters)

# 使用 del 也可以删除

tanks = ['亚瑟', '程咬金', '盾山', '张飞', '廉颇','廉颇']
# 查询相关的方法  index  元素不存在报错
print(tanks.index('盾山'))
# print(tanks.index('庄周'))
print(tanks.count('廉颇'))

# in 运算符

print('庄周' in tanks)

# 修改元素
# 使用下标直接修改列表的元素
