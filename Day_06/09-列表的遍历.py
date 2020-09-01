# 将所有的数据访问一边 遍历针对的是 可迭代对象

# while / for in
killers = ['李白', '兰陵王', '韩信', '孙悟空', '赵云']

# for...in 循环是不断的调用迭代器 next查找下一个数据
for k in killers:
    print(k)

i = 0
while i < len(killers):
    print(killers[i])
    i += 1
