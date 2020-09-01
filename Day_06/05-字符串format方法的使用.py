# {} 占位

a = '{},{}'.format('张三', 19)
print(a)

# {数字} 根据数字的顺序进行填入

b = '{1},{0}'.format('张三', 19)
print(b)
# {变量名}
d = '{age},{name}'.format(age=19, name='ll')
print(d)

# 混合使用{数字} {变量}  注意 变量要写在后面
# {} {数字}不能混合使用
# 与列表配合使用
f = ['ll', '上海', '190']
# g = '我的名字是{}，我来自{},身高{}'.format(f[0], f[1], f[2])#
g = '我的名字是{}，我来自{},身高{}'.format(*f)
print(g)

# 与字典配合使用
info = {'name': 'll', 'age': 19, 'addr': '上海'}
h = '{name},{age},{addr}'.format(**info)
print(h)