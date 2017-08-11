# -- coding: utf-8 --

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)

