# split,splitlines,partition和rpartition

# split 将一个字符串切割为一个列表,两个参数，最后一个是最大分割数
# rsplit('-',2)是将最后两位的字符分隔成列表
# a = 'hey-you-must-be-happy'
# b = a.split('-')
# print(b)
#
# c = a.rsplit('-', 2)
# print(c)

a = 'abcdFeghj'
# partition 分为三部分 前面，分隔符 后面,分割之后是一个元组
print('abcdFeghj'.partition('F'))
