# -- coding: utf-8 --
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volumn = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_volumn = max(max_volumn, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_volumn
