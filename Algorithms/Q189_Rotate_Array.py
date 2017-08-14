# encoding: utf-8

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        shift_places = k % len(nums)
        head = nums[-shift_places:]
        tail = nums[:-shift_places]
        nums[:] = head + tail

