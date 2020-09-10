nums = [8, 96, 2, 9]

# 第一种 nums 排序取最后一个

# nums.sort()
# print(nums[-1])
# print(nums)

# nums降序之后取第一个
# nums.sort(reverse=True)
# print(nums[0])

# 假设法，如果假设第一个数为最大数，与列表中的元素进行比较
x = nums[0]
for i in nums:
    if i > x:
        x = i
print(x, nums.index(x))
