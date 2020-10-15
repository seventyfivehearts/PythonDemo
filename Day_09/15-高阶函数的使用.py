# 1.一个函数作为另一个函数的参数
# 2.一个函数作为另一个函数的返回值
# 3.在一个函数中写另一个函数

def foo():
    print(1)
    return 'foo'


def bar():
    print(2)
    return foo


x = bar()
print('x的值是{}'.format(x))

print('-----------------')
x()

bar()()  # 调用bar · bar再调用foo


def outer():
    m = 100

    def inner():
        n = 98
        print('我是inner函数')

    inner()
    print('我是outer函数')
    return inner


# inner()函数在外部不能使用
outer()()  # 先调用outer 再在outer内部调用inner
