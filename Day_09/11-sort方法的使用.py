nums = [3, 4, 5, 6, 9, 0, 12]

# 列表的sort方法,会直接对列表进行排序,之后列表会改变的
# nums.sort()
# print(nums)

# sorted 为内置函数,不会改变原有的数据,而是生成一个新的列表
a = sorted(nums)
print(nums)
print(a)

students = [
    {'name': 'zhangsan', 'age': 18, 'height': 183, 'score': 100},
    {'name': 'lisi', 'age': 19, 'height': 185, 'score': 90},
    {'name': 'wangwu', 'age': 20, 'height': 175, 'score': 80},
    {'name': 'sunliu', 'age': 22, 'height': 176, 'score': 78}

]


def foo(foo):
    return foo['age']


students.sort(key=foo)
students.sort(key=lambda foo: foo['age'])
print(students)
