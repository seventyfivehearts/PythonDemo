a = 'abcdefghijklmn'
print(len(a))
# 查找内容的相关方法 find/index/rfind/rindex
print(a.find('l'))  # 获取指定字符的下标

print(a.index('l'))

# index find 区别
print(a.index('p'))
print(a.find('p'))
# find 找不到元素会返回 -1 index会报错
