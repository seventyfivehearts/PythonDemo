# 使用简单的语法创建列表
# nums = [i for i in range(10)]
# print(nums)
#
# # 取所有的偶数
# x = [i for i in range(10) if i % 2 == 0]
# print(x)
#
# points = [(x,y) for x in range(10) for y in range(10)]
# print(points)
# 生成1到100的数字
m = [i for i in range(1, 101)]
n = [m[j: j + 3] for j in range(0, 100,3)]
print(m)
print(n)
