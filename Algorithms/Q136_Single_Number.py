# -- coding: utf-8 --

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        collection = {}
        for num in nums:
            if num in collection:
                collection.pop(num)
            else:
                collection[num] = 1
        return collection.keys()[0]



