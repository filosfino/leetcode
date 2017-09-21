# -- coding: utf-8 --

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = 0
        while index < len(nums)-count:
            if nums[index] == 0:
                nums.append(nums.pop(index))
                count += 1
            else:
                index += 1





