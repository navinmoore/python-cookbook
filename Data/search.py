# -*- coding:utf-8 -*-
# author: wangzhiyao


def binary_search(temp_list, item):
    """
    二分法 查找
    :param temp_list:
    :param item:
    :return:
    """
    if not temp_list:
        return
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 10]
    print binary_search(my_list, 3)
