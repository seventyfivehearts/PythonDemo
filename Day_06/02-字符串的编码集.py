
# ASCII --> Latin1--> Unicode编码

# 字符 --》数字编码存在一个对应的关系
# 使用内置函数 chr 和 ord 可以查看数字和字符的对应的关系
# ord 获取字符对应的编码, chr根据编码获取对应的字符

print(ord('a'))


# GBK utf-8 BIG5

print('你'.encode('gbk'))


# encode 将字符串转换为指定编码集
# decode 将编码集转换成为对应的字符
