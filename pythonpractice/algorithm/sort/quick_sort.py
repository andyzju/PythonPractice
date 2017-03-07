# coding=utf-8


"""
想法一：它选择第一个元素作为主元，它同样可以按照下面提到的算法导论中将数组分成了4个不同的部分，
但是这里其实有更好的解释方法。首先，它每次都是选择第一个元素都为主元，这个回合就是要确定主元的位置；
然后，有两个指针，一个leftmark指向主元的后面一个位置，另一个rightmark指向要排序的数组最后一个元素；
接着，两个指针分别向中间移动，leftmark遇到比主元大的元素停止，rightmark遇到比主元小的元素停止，
如果此时leftmark<rightmark，也就是说中间还有未处理(未确定与主元大小关系)的元素，
那么就交换leftmark和rightmark位置上的元素，然后重复刚才的移动操作，直到rightmark<leftmark；
最后，停止移动时候rightmark就是主元要放置的位置，因为它停在一个比主元小的元素的位置上，
之后交换主元和rightmark指向的元素即可。完了之后，递归地对主元左右两边的数组进行排序即可。

快速排序三点：  o(nlogn)
1. 递归排序；
2. 找每个子集第一个元素的正确排序位置，从其后至最后，两边开始搜索位置，将小于置于其前，大于置于其后;(交换)
3. 将元素交换至合适位置（right）
4. 递归左右子集
"""


class QuickSort(object):

    def quick_sort(self, lst):
        self.quick_sort_helper(lst, 0, len(lst)-1)

    def quick_sort_helper(self, lst, first, last):
        if first < last:
            pivot_position = self.partition(lst, first, last)
            self.quick_sort_helper(lst, first, pivot_position - 1)
            self.quick_sort_helper(lst, pivot_position + 1, last)

    def partition(self, lst, first, last):

        # 每次把first作为要排序到正确位置的元素
        value = lst[first]
        left = first + 1
        right = last
        while left <= right:
            while left <= right and lst[left] <= value:  # 找到第一个>=1的数
                left += 1
            # 上述找到第一个>= value 的位置

            while left <= right and lst[right] >= value:  # 从右边找第一个小于value的值
                right -= 1

            # 找到值进行交换
            if left <= right:  # 这个判断为什么如此重要
                lst[left], lst[right] = lst[right], lst[left]

        # 循环结束之后，right位置左边都小于value，右边都大于value
        lst[first], lst[right] = lst[right], lst[first]
        return right

if __name__ == "__main__":
    qs = QuickSort()
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    qs.quick_sort(a_list)
    print(a_list)

