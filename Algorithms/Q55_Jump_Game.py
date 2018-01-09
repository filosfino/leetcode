# -- coding: utf-8 --

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps_remaining = 0
        length = len(nums)
        for i, num in enumerate(nums):
            steps_remaining = max(steps_remaining-1, num)
            if steps_remaining + i >= length-1:
                return True
            if steps_remaining <= 0:
                return False
        return steps_remaining >= 0
