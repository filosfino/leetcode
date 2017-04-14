# encoding: utf-8


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if target-n in d:
                ret = [d[target-n], i]
                break
            d[n] = i
        else:
            raise Exception

        return ret
