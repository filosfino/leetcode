# -- coding: utf-8 --
from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp = defaultdict(list)
        for i, num in enumerate(nums):
            if num not in tmp:
                tmp[num].append(i)
            else:
                if i-tmp[num][-1] <= k:
                    return True
                tmp[num].append(i)
        return False



