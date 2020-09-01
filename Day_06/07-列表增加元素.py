# 列表的操作，有序 可变的
# 增加 删除 修改 查询
# 增删改查
hero = ['李白', '韩信', '后裔', '李元芳']

# 添加元素的方法
# append insert extend
# append 在列表的最后面追加一个数据
hero.append('赵云')
print(hero)

# insert(index, object) 需要两个参数
# index 表示下标，在那个位置插入数据
# object 表示插入的数据
hero.insert(2, '王昭君')
print(hero)

# extend(iterable) 需要一个可迭代对象
# a.extend(b) 把b添加到a里面  b不变
a = ['马克菠萝', '狄仁杰']
hero.extend(a)
print(hero)
print(a)
