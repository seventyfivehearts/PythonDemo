x = ['hello', 'hey', '', 'world']
# 把空的字符串都取消掉
for words in x:
    if words == '':
        x.remove(words)

print(x)





