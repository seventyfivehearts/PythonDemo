# # 输入一个名字，存在打印已存在，不存在则加入列表中
#
# name = ['zhangsan', 'lisi', 'carter', 'wangwu']
# username = input('请输入用户名:')
# if username in name:
#     print('用户存在')
# else:
#     name.append(username)
#
# print(name)

nums = [6, 5, 3, 1, 8, 7, 2, 4]
j = 0
count = 0
while j < len(nums) - 1:

    i = 0
    while i < len(nums) - 1 - j:
        count += 1
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
    j += 1
print(nums)
print(count)
