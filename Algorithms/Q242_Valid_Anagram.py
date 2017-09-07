# -- coding: utf-8 --
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        diff_count = defaultdict(lambda: 0)
        for i in range(len(s)):
            diff_count[s[i]] += 1
            diff_count[t[i]] -= 1
        return not any(diff_count.values())


