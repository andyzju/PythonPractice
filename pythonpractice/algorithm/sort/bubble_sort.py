# coding=utf-8

"""
冒泡排序(bubble sort)：每个回合都从第一个元素开始和它后面的元素比较，
如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
每次遍历都将剩下的元素中最大的那个放到了序列的“最后”(除去了前面已经排好的那些元素)。
注意检测是否已经完成了排序，如果已完成就可以退出了。
时间复杂度$O(n^2)$
"""


class BufferSort(object):
    # 默认升序排序
    @staticmethod
    def sort(lst):
        n = len(lst)
        for i in range(n-1):
            for j in range(n-1-i):
                left = lst[j]
                right = lst[j+1]
                if left > right:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    @staticmethod
    def sort_2(a_list):
        pass_num = len(a_list) - 1
        while pass_num > 0:
            for i in range(pass_num):
                if a_list[i] > a_list[i + 1]:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
            pass_num -= 1

        return a_list

if __name__ == "__main__":

    a = [12, 9, 232, 4343, 5, 8, 9, 0, 2, 555]
    print BufferSort.sort(a)

    print BufferSort.sort_2(a)



