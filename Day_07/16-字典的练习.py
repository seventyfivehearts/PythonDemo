chars = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'c', 'd']

chars_count = {}
# for char in chars:
#     if char in chars_count:
#         chars_count[char] += 1
#     else:
#         chars_count[char] = 1
# print(chars_count)

for char in chars:
    if char not in chars_count:
        chars_count[char] = chars.count(char)
print(chars_count)
