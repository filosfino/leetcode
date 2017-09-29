# -- coding: utf-8 --

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []

        while 1:
            if nums1 and nums2:
                if nums1[-1] > nums2[-1]:
                    nums1.pop()
                elif nums2[-1] > nums1[-1]:
                    nums2.pop()
                else:
                    val = nums1.pop()
                    nums2.pop()
                    result.append(val)
            else:
                break
        return result


