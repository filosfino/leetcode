class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if not length:
            return -1
        if target < nums[0]:
            i = length-1
            while i > 0 and target < nums[i] and nums[i-1] < nums[i]:
                i -= 1
            if target == nums[i]:
                return i
            else:
                return -1
        else:
            i = 0
            while i < length-1 and target > nums[i] and nums[i+1] > nums[i]:
                i += 1
            if target == nums[i]:
                return i
            else:
                return -1
