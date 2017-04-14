# -- coding: utf-8 --


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        previous_index = 0
        current_index = 1
        count = 1
        length = len(nums)

        while 1:
            if nums[current_index] != nums[previous_index]:
                previous_index = current_index
                count += 1
                current_index += 1
            else:
                nums.pop(current_index)
                length -= 1

            if current_index == length:
                break

        return count


