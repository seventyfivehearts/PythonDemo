nums = {'a': 100, 'b': 200, 'c': 300}  # 需求 --> {'100':a,'200':b,'300':c }
# 思路,新建一个空字典
nums1 = {}
for k, v in nums.items():
    nums1[v] = k
print(nums1)

# 使用字典推导式
dict1 = {v: k for v, k in nums.items()}
print(dict1)
