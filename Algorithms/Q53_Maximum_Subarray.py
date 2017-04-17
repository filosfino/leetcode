# -- coding: utf-8 --


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        current_index = 0
        max_sum_ending_previous = 0
        max_sum = nums[current_index]

        while current_index < len(nums):
            max_sum_ending_previous = max([
                max_sum_ending_previous+nums[current_index],
                nums[current_index]
            ])
            max_sum = max([max_sum, max_sum_ending_previous])
            current_index += 1

        return max_sum
