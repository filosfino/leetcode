# -- coding: utf-8 --

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        previous, now = 0, 0
        for i in nums:
            previous, now = now, max(now, previous+i)
        return now




