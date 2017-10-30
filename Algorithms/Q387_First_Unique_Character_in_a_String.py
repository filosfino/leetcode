# -- coding: utf-8 --
import string


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_letters = [l for l in string.ascii_lowercase if s.count(l)==1]
        unique_index = [s.index(l) for l in unique_letters]
        return min(unique_index) if unique_index else -1




