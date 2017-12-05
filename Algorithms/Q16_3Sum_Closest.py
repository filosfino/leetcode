# encoding: utf-8
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        s = nums[0] + nums[1] + nums[2]
        # print(nums)
        # print(list(range(len(nums))))
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum - target == 0:
                    return sum
                if abs(s - target) > abs(sum - target):
                    s = sum
                if sum < target:
                    l += 1
                else:
                    r -= 1
        return s
