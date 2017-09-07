# -- coding: utf-8 --

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>=0 and '{:b}'.format(n).count('1')==1
