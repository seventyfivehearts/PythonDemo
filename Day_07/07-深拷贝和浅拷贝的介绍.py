import copy

words = ['hello', 'happy', 'hey', [100, 200, 300], 'hi']

# 浅拷贝  浅拷贝认为只拷贝了一层

words1 = words.copy()
print(words1)
# 深拷贝
words2 = copy.deepcopy(words)
print(words2)
