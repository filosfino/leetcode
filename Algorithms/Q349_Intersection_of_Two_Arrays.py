# -- coding: utf-8 --

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = {}
        result = set()
        for i in nums1:
            tmp.setdefault(i, 1)
        for i in nums2:
            if i in tmp and i not in result:
                result.add(i)
        return list(result)


