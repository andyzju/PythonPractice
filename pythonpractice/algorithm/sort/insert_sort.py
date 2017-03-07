# coding=utf-8



class InsertSort(object):

    @staticmethod
    def sort(lst):

        for index in range(1, len(lst)):  # 假设第一个已经排序好
            current_value = lst[index]  # 需要插入值
            position = index
            while position > 0 and lst[position-1] > current_value:
                lst[position] = lst[position-1]  # 将最大的值移到插入位置
                position -= 1

            lst[position] = current_value
        return lst

if __name__ == "__main__":

    a = [12, 9, 232, 4343, 5, 8, 9, 0, 2, 555]
    print InsertSort.sort(a)


