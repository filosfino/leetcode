class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return
        if nums[-2] < nums[-1]:
            self.swap(nums, -2, -1)
        else:
            i = length - 1
            while i > 0 and nums[i-1] >= nums[i]:
                i -= 1
            if i == 0:
                nums.sort()
            else:
                current_head = i-1
                count = 0
                while current_head < length-1 and nums[current_head+1] > nums[current_head]:
                    self.swap(nums, current_head, current_head+1)
                    current_head += 1
                    count += 1
                next_head = current_head - 1
                for _ in range(count-1):
                    self.swap(nums, next_head-1, next_head)
                    next_head -= 1
                nums[i:] = nums[i:][::-1]

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
