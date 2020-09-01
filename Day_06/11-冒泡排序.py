# nums = [6, 5, 3, 1, 8, 7, 2, 4]
# for i in range(0, len(nums)-1):
#     for j in range(0, len(nums) - 1-i):
#         if nums[j] > nums[j + 1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#
# print(nums)
# nums = [5, 1, 7, 6, 8, 2, 4, 3]
#
# for j in range(0, len(nums) - 1):
#     for i in range(0, len(nums) - 1 - j):
#         if nums[i] > nums[i + 1]:
#             a = nums[i]
#             nums[i] = nums[i + 1]
#             nums[i + 1] = a
#
# print(nums)
nums = [5, 1, 7, 6, 8, 2, 4, 3]
i = 0
while i < len(nums) - 1:
    i += 1
    n = 0
    while n < len(nums) - 1:
        if nums[n] > nums[n + 1]:
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
        n += 1
print(nums)
