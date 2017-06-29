# coding=utf-8

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 代表着输出这个值
        # print b
        a, b = b, a + b
        n = n + 1


print fab(5)
for x in fab(5):
    print x

f = fab(3)
