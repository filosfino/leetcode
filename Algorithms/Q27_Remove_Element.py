# -- coding: utf-8 --


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return 0

        index = 0
        while 1:
            if nums[index] == val:
                nums.pop(index)
                length -= 1
            else:
                index += 1

            if index == length:
                break

        return length

