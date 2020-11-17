# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 15:28
# @Author  : sunzhen
# @File    : 01-二分法.py
# @Software: PyCharm

# 算法:最高效解决问题的方法

# 算法之二分法

# 需求:有一个按照从小到大排序的数字列表
# 需要从该列表中找到我么想要的数字,如何更高效??

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
find_num = 17


# 方案一,整体遍历效率太低
# for num in nums:
#     if find_num == num:
#         print('find it')
#         break


# 方案二. 二分法
def func(find_num, l):
    print(l)
    if len(l) == 0:
        print('找的值不存在')
        return
    mid_index = len(l) // 2
    mid_val = l[mid_index]
    if find_num > mid_val:
        #     接下来查找中间值右边的值
        l = l[mid_index + 1:]
        func(find_num, l)
    elif find_num < mid_val:
        #     接下来查找中间值左边的位置
        l = l[:mid_index]
        func(find_num, l)
    else:
       print('find it')

func(find_num,nums)