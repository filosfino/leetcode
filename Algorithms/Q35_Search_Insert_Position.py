# -- coding: utf-8 --


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        pos = 0
        while pos < len(nums):
            if nums[pos] >= target:
                return pos
            pos += 1
        return len(nums)

    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return int(target >= nums[0])
        elif len(nums) == 2:
            if target > nums[1]:
                return 2
            elif nums[0] < target <= nums[1]:
                return 1
            else:
                return 0

        middle_index = int(len(nums) / 2)

        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            return self.searchInsert2(nums[:middle_index], target)
        else:
            return self.searchInsert2(nums[middle_index:], target) + middle_index + 1


