# -- coding: utf-8 --

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        current_sum = 0
        self.sums = []
        for n in nums:
            current_sum += n
            self.sums.append(current_sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)