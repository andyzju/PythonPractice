# coding=utf-8
from collections import defaultdict

"""
计数排序：在数的范围很小时还是不错的，当数的范围很大的时候就不适用了，
计数排序一般用于基数排序中。需要注意的是，计数完了之后进行插入时，
为了保证排序的稳定性，需要从后往前插入。
o(n)
仅仅适用于数值大小不够的情况；
"""


# TODO
class BaseSort(object):

    @staticmethod
    def counting_sort(A, key=lambda x: x):
        count_list = [], defaultdict(list)
        for x in A:
            count_list[x] += 1
        print count_list

if __name__ == "__main__":
    seq = [12, 9, 232, 4343, 5, 8, 9, 0, 2, 555]
    seq = BaseSort.counting_sort(seq)