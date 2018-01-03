class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not enumerate:
            return []

        nums = sorted(nums)
        return self._permuteUnique(nums)

    def _permuteUnique(self, nums):
        if not nums:
            return [[]]
        ret = []
        for i, n in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            ret.extend([[n] + p for p in self._permuteUnique(nums[:i]+nums[i+1:])])
        return ret

