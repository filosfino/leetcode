# -*- coding: utf-8 -*-

def get_median(l):
    # print('get_median %s' % l)
    length = len(l)

    if length == 0:
        raise Exception

    if length == 1:
        return l[0]
    elif length % 2 == 0:
        median_position_1 = (length - 1) // 2
        median_position_2 = median_position_1 + 1
        return float(l[median_position_1] + l[median_position_2]) / 2
    else:
        return l[int((length - 1) / 2)]


def bisection_insert_extend(base_list, insert_list):
    start_index = 0
    for i in insert_list:
        # print('inserting element: %s' % i)
        # print('locals: %s' % locals())
        inserted_index = bisection_insert(base_list, start_index, len(base_list) - 1, i)
        # print('inserted at %s, now list is: %s' % (inserted_index, base_list))
        start_index = inserted_index


def bisection_insert(base_list, l, u, element):
    # 在两边之外
    if element <= base_list[l]:
        base_list.insert(l, element)
        return l
    elif base_list[u] < element:
        base_list.insert(u + 1, element)
        return u

    while 1:
        # 小于两个不分
        if u - l <= 1:
            if base_list[l] == element:
                base_list.insert(l, element)
                return l
            else:
                base_list.insert(u, element)
                return u

        s = l + u
        middle = s / 2 if s % 2 == 0 else (s - 1) / 2

        if base_list[l] <= element < base_list[middle]:
            inserted_index = bisection_insert(base_list, l, middle, element)
            # print(base_list)
            return inserted_index
        elif base_list[middle] < element <= base_list[u]:
            inserted_index = bisection_insert(base_list, middle, u, element)
            # print(base_list)
            return inserted_index
        elif element == base_list[middle]:
            base_list.insert(middle, element)
            return middle


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 == 0:
            return get_median(nums2)
        if len2 == 0:
            return get_median(nums1)

        base_list = nums1 if len1 >= len2 else nums2
        insert_list = nums2 if len1 >= len2 else nums1

        bisection_insert_extend(base_list, insert_list)
        return get_median(base_list)
