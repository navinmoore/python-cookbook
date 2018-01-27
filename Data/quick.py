# -*- coding:utf-8 -*-
# author: wangzhiyao


def quick(arr):
    """
    快速排序 O(nlogn)
    :param arr:
    :return:
    """
    if len(arr) > 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quick(less) + [pivot] + quick(great)