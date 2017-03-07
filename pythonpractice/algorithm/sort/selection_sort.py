# coding=utf-8

"""
选择排序(selection sort)：每个回合都选择出剩下的元素中最大的那个，
选择的方法是首先默认第一元素是最大的，如果后面的元素比它大的话，
那就更新剩下的最大的元素值，找到剩下元素中最大的之后将它放入到合适的位置就行了。
和冒泡排序类似，只是找剩下的元素中最大的方式不同而已。时间复杂度$O(n^2)$

[每次选择最大的放到最后]
"""


class SelectionSort(object):

    @staticmethod
    def sort(lst):
        n = len(lst)
        for i in range(n):  # 选择n-1次数
            max_position = n-1-i
            max_value_position = max_position
            for j in range(max_position):
                if lst[j] > lst[max_value_position]:
                    max_value_position = j
            lst[max_value_position], lst[max_position] = lst[max_position], lst[max_value_position]
        return lst


if __name__ == "__main__":

    a = [12, 91, 232, 4343, 5, 8, 9, 0, 2, 555]
    print SelectionSort.sort(a)
