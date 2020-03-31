def deco(func):
    def inner(*args):
        print('args is:', args)
        return func(*args)

    return inner


@deco
def test(a, b):
    print('in test')
    return a * b


print(test(4, 5))

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='89898')

str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-4:-1])  # 45
print(str2[3:1])
print(str2[4:1])
