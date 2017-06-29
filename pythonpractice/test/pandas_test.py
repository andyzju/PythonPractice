# coding=utf-8
from numpy import *

# 递归深度问题
# 数值超过int范围
class Cheng(object):

    @staticmethod
    def micheng(x, num):
        if num == 0:
            return 1
        if num == 1:
            return x
        return Cheng.micheng(x, num-1) * x

if __name__ == "__main__":

    x = matrix([[long(2), long(3)],
                [long(6), long(7)]])

    print Cheng.micheng(x, 9)

