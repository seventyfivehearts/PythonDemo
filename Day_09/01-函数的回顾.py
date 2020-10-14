# 函数名 标识符
def get_sum(a, b):
    return a + b


x = get_sum(1, 2)
print(x)


def calc(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


a = calc(1, 6)
print(a)
